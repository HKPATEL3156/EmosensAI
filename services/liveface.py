import av
import cv2

from streamlit_webrtc import VideoProcessorBase

from services.face_service import predict_face


face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


class LiveFace(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(format="bgr24")

        gray = cv2.cvtColor(
            img,
            cv2.COLOR_BGR2GRAY
        )

        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(80, 80)
        )

        for (x, y, w, h) in faces:

            face = img[
                y:y+h,
                x:x+w
            ]

            emo, conf = predict_face(face)

            cv2.rectangle(
                img,
                (x, y),
                (x+w, y+h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                img,
                f"{emo} {conf:.1f}%",
                (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

        return av.VideoFrame.from_ndarray(
            img,
            format="bgr24"
        )