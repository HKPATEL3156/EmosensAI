import streamlit as st
import cv2
import numpy as np

from PIL import Image
from streamlit_webrtc import webrtc_streamer

from services.face_service import predict_face
from services.face_service import load_face_model
from services.liveface import LiveFace


load_face_model()


def face():

    st.title("Face Emotion Detection")

    st.caption(
        "Detect human emotions using image upload or live webcam."
    )

    st.divider()

    left, right = st.columns(2, gap="large")

    # ---------------- Upload ---------------- #

    with left:

        st.subheader("Image Upload")

        img = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"]
        )

        if img:

            pic = Image.open(img)

            st.image(
                pic,
                use_container_width=True
            )

            if st.button(
                "Predict Emotion",
                use_container_width=True
            ):

                img_np = np.array(pic)

                img_cv = cv2.cvtColor(
                    img_np,
                    cv2.COLOR_RGB2BGR
                )

                emo, conf = predict_face(img_cv)

                st.session_state["emo"] = emo
                st.session_state["conf"] = conf

        else:

            st.info(
                "Upload an image to begin."
            )

    # ---------------- Live ---------------- #

    with right:

        st.subheader("Live Detection")

        webrtc_streamer(
            key="face_live",
            video_processor_factory=LiveFace,
            media_stream_constraints={
                "video": True,
                "audio": False
            }
        )

    st.divider()

    st.subheader("Prediction Result")

    emo = st.session_state.get("emo", "--")
    conf = st.session_state.get("conf", "--")

    status = "Ready"

    if emo == "--":
        status = "Waiting"

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Emotion",
        emo.title() if emo != "--" else "--"
    )

    c2.metric(
        "Confidence",
        f"{conf:.2f}%"
        if conf != "--"
        else "--"
    )

    c3.metric(
        "Status",
        status
    )