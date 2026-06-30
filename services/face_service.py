import cv2
import numpy as np


model_path = "ml-services/models/emotion_model.h5"

emotion = [
    "angry",
    "disgust",
    "fear",
    "happy",
    "neutral",
    "sad",
    "surprise"
]


model = None


def load_face_model():
    global model

    if model is None:
        try:
            from tensorflow.keras.models import load_model
        except Exception as exc:
            raise RuntimeError(
                "TensorFlow is not available or incompatible in this environment."
            ) from exc

        model = load_model(model_path)

    return model


def preprocess(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.resize(img, (48, 48))

    img = img.astype("float32") / 255.0

    img = np.expand_dims(img, axis=-1)

    img = np.expand_dims(img, axis=0)

    return img


def predict_face(img):
    try:
        net = load_face_model()
    except Exception:
        return "neutral", 0.0

    img = preprocess(img)
    pred = net.predict(img, verbose=0)

    idx = np.argmax(pred)
    emo = emotion[idx]
    conf = float(pred[0][idx] * 100)

    return emo, conf
 
 