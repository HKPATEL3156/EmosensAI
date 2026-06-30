import os
import tempfile
import threading

import av
import numpy as np
import soundfile as sf

from streamlit_webrtc import AudioProcessorBase

from services.speech_service import predict_speech


class LiveSpeech(AudioProcessorBase):

    def __init__(self):
        self.buffer = []
        self.fs = 16000
        self.chunk_seconds = 1.0
        self.emo = "--"
        self.conf = 0.0
        self.busy = False
        print("\n========== LiveSpeech Started ==========\n")

    def predict(self, path):
        try:
            emo, conf = predict_speech(path)
            self.emo = emo
            self.conf = conf
            print("--------------------------------")
            print("Emotion    :", emo)
            print("Confidence :", conf)
            print("--------------------------------")
        except Exception as e:
            print(e)
        finally:
            try:
                os.unlink(path)
            except OSError:
                pass
            self.busy = False

    def recv(self, frame):
        audio = frame.to_ndarray()

        if len(audio.shape) == 2:
            if audio.shape[0] == 1:
                audio = audio.flatten()
            else:
                audio = audio.mean(axis=1)
        else:
            audio = audio.reshape(-1)

        self.buffer.extend(np.asarray(audio, dtype=np.float32).tolist())

        if len(self.buffer) >= self.fs * self.chunk_seconds and not self.busy:
            self.busy = True

            chunk = np.array(
                self.buffer[-int(self.fs * self.chunk_seconds):],
                dtype=np.float32,
            )
            self.buffer = self.buffer[-int(self.fs * 0.25):]

            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            sf.write(temp.name, chunk, self.fs)
            temp.close()

            threading.Thread(
                target=self.predict,
                args=(temp.name,),
                daemon=True,
            ).start()

        return frame