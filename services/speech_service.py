from pathlib import Path

import joblib
import librosa
import numpy as np
import torch

from transformers import (
    AutoModelForAudioClassification,
    AutoProcessor,
)


import streamlit as st

base = Path(__file__).resolve().parent.parent
model_path = base / "ml-services" / "models" / "speech_emotion"


def normalize_audio_input(audio, sample_rate, max_len=32000):
    audio = np.asarray(audio, dtype=np.float32)

    if audio.ndim > 1:
        audio = np.mean(audio, axis=1)

    audio = np.reshape(audio, (-1,))

    if sample_rate != 16000:
        audio = librosa.resample(audio, orig_sr=sample_rate, target_sr=16000)

    # Pad or truncate to exactly 32000 samples (2 seconds) to match training
    if len(audio) > max_len:
        audio = audio[:max_len]
    else:
        audio = np.pad(
            audio,
            (0, max_len - len(audio)),
            mode="constant"
        )

    return audio.astype(np.float32)


@st.cache_resource
def load_speech_model():
    print("Loading Speech Model...")
    device = "cuda" if torch.cuda.is_available() else "cpu"

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
    return processor, model, label_map, device


def predict_speech(audio_path, return_all=False):
    print("Predict Called")

    processor, model, label_map, device = load_speech_model()

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

    prob = torch.softmax(outputs.logits, dim=-1)[0]
    idx = torch.argmax(prob, dim=-1).item()

    inv_map = {v: k for k, v in label_map.items()}
    emo = inv_map[idx]
    conf = float(prob[idx] * 100)

    if return_all:
        prob_dict = {inv_map[i]: float(prob[i] * 100) for i in range(len(prob))}
        return emo, conf, prob_dict

    return emo, conf
