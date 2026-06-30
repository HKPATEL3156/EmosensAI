import os
import tempfile
import threading

import av
import numpy as np
import soundfile as sf
import librosa

from streamlit_webrtc import AudioProcessorBase

from services.speech_service import predict_speech


class LiveSpeech(AudioProcessorBase):

    def __init__(self):
        self.buffer = []
        self.buffer_len = 0
        self.in_sample_rate = None
        self.chunk_seconds = 1.5
        self.emo = "--"
        self.conf = 0.0
        self.busy = False
        print("\n========== LiveSpeech Started ==========\n")

    def predict(self, chunk, sr):
        temp_path = None
        try:
            # Resample in the background thread
            if sr != 16000:
                chunk = librosa.resample(chunk, orig_sr=sr, target_sr=16000)

            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            temp_path = temp.name
            sf.write(temp_path, chunk, 16000)
            temp.close()

            emo, conf = predict_speech(temp_path)
            self.emo = emo
            self.conf = conf
            print("--------------------------------")
            print("Emotion    :", emo)
            print("Confidence :", conf)
            print("--------------------------------")
        except Exception as e:
            print(f"Error in LiveSpeech predict: {e}")
        finally:
            if temp_path and os.path.exists(temp_path):
                try:
                    os.unlink(temp_path)
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

        audio = np.asarray(audio, dtype=np.float32)
        self.buffer.append(audio)
        self.buffer_len += len(audio)

        if self.in_sample_rate is None:
            self.in_sample_rate = frame.sample_rate

        # 1.5 seconds of audio at input sample rate
        chunk_samples = int(self.in_sample_rate * self.chunk_seconds)

        if self.buffer_len >= chunk_samples and not self.busy:
            self.busy = True

            # Concatenate all buffered arrays
            full_buffer = np.concatenate(self.buffer)
            # Take the last chunk_samples
            chunk = full_buffer[-chunk_samples:]
            
            # Keep the last 0.25 seconds of audio for overlap
            overlap_samples = int(self.in_sample_rate * 0.25)
            self.buffer = [full_buffer[-overlap_samples:]]
            self.buffer_len = overlap_samples

            threading.Thread(
                target=self.predict,
                args=(chunk, self.in_sample_rate),
                daemon=True,
            ).start()

        return frame
