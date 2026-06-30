from pathlib import Path

import joblib
import librosa
import numpy as np
import torch

from transformers import (
    AutoModelForAudioClassification,
    AutoProcessor,
)


base = Path(__file__).resolve().parent.parent
model_path = base / "ml-services" / "models" / "speech_emotion"

processor = None
model = None
label_map = None
device = "cuda" if torch.cuda.is_available() else "cpu"


def normalize_audio_input(audio, sample_rate):
    audio = np.asarray(audio, dtype=np.float32)

    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    audio = np.reshape(audio, (-1,))

    if sample_rate != 16000:
        audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=16000)

    return audio.astype(np.float32)


def load_speech_model():
    print("Loading Speech Model...")

    global processor
    global model
    global label_map
    global device

    if processor is None or model is None:
        processor = AutoProcessor.from_pretrained(
            model_path,
            local_files_only=True,
        )

        torch_dtype = torch.float16 if device == "cuda" else torch.float32

        model = AutoModelForAudioClassification.from_pretrained(
            model_path,
            local_files_only=True,
            torch_dtype=torch_dtype,
        )

        model.to(device)
        model.eval()

        label_map = joblib.load(model_path / "label_map.pkl")


def predict_speech(audio_path):
    print("Predict Called")

    load_speech_model()

    audio, sr = librosa.load(audio_path, sr=None, mono=True)
    audio = normalize_audio_input(audio, sr)

    inputs = processor(
        audio,
        sampling_rate=16000,
        return_tensors="pt",
        padding=True,
    )

    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.inference_mode():
        outputs = model(**inputs)

    prob = torch.softmax(outputs.logits, dim=-1)
    idx = torch.argmax(prob, dim=-1).item()

    inv_map = {v: k for k, v in label_map.items()}
    emo = inv_map[idx]
    conf = float(prob[0][idx] * 100)

    return emo, conf