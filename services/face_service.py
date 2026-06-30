import cv2
import numpy as np


from pathlib import Path

base = Path(__file__).resolve().parent.parent
model_path = str(base / "ml-services" / "models" / "emotion_model.h5")

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


def predict_face(img, return_all=False):
    try:
        net = load_face_model()
    except Exception:
        if return_all:
            return "neutral", 0.0, {e: 0.0 for e in emotion}
        return "neutral", 0.0

    img = preprocess(img)
    pred = net.predict(img, verbose=0)

    idx = np.argmax(pred)
    emo = emotion[idx]
    conf = float(pred[0][idx] * 100)

    if return_all:
        prob_dict = {emotion[i]: float(pred[0][i] * 100) for i in range(len(emotion))}
        return emo, conf, prob_dict

    return emo, conf


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def extract_face(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(45, 45)
    )
    if len(faces) > 0:
        # Sort by area and get the largest face
        x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
        return img[y:y+h, x:x+w], (x, y, w, h)
    return None, None


 
 