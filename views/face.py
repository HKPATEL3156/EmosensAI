import streamlit as st
import cv2
import numpy as np
import pandas as pd
from PIL import Image
from streamlit_webrtc import webrtc_streamer

from services.face_service import predict_face, load_face_model, extract_face
from services.liveface import LiveFace

load_face_model()


def face():
    st.title("👤 Face Emotion Detection")
    st.caption(
        "Detect human emotions from facial expressions using image upload or live webcam."
    )

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    left, right = st.columns(2, gap="large")

    # ---------------- Upload ---------------- #
    with left:
        st.subheader("📸 Image Upload")
        st.caption("Upload a photo containing a face to analyze expression.")

        img_file = st.file_uploader(
            "Choose an image",
            type=["jpg", "jpeg", "png"],
            key="face_upload"
        )

        if img_file:
            pic = Image.open(img_file)
            img_np = np.array(pic)
            img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Detect face
            face_img, bbox = extract_face(img_cv)

            if face_img is not None:
                x, y, w, h = bbox
                # Draw a beautiful bounding box on a copy
                annotated_img = img_cv.copy()
                cv2.rectangle(
                    annotated_img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    4
                )
                # Convert back to RGB for displaying
                display_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
                st.image(display_img, width="stretch", caption="Face Detected!")
            else:
                st.image(pic, width="stretch")
                st.warning("No face detected. The model will analyze the entire image.")

            if st.button("Predict Emotion", width="stretch", key="predict_face_btn"):
                # Predict on cropped face if available, otherwise whole image
                target_img = face_img if face_img is not None else img_cv
                emo, conf, probs = predict_face(target_img, return_all=True)

                st.session_state["face_emo"] = emo
                st.session_state["face_conf"] = conf
                st.session_state["face_probs"] = probs
        else:
            st.info("Upload an image to begin.")

    # ---------------- Live ---------------- #
    with right:
        st.subheader("🎥 Live Webcam")
        st.caption("Start your webcam to see real-time facial expression tracking.")

        webrtc_streamer(
            key="face_live",
            video_processor_factory=LiveFace,
            media_stream_constraints={
                "video": True,
                "audio": False
            }
        )

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    # ---------------- Results ---------------- #
    st.subheader("🔮 Prediction Results")

    emo = st.session_state.get("face_emo", "--")
    conf = st.session_state.get("face_conf", "--")
    probs = st.session_state.get("face_probs", None)

    emoji_map = {
        "angry": "😡",
        "disgust": "🤢",
        "fear": "😨",
        "happy": "😊",
        "neutral": "😐",
        "sad": "😢",
        "surprise": "😲"
    }

    status = "Ready" if emo != "--" else "Waiting"

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Emotion",
        f"{emoji_map.get(emo, '')} {emo.title()}" if emo != "--" else "--"
    )

    c2.metric(
        "Confidence",
        f"{conf:.2f}%" if conf != "--" else "--"
    )

    c3.metric(
        "Status",
        status
    )

    # Display probabilities chart if available
    if probs:
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("📊 **Emotion Probability Distribution**")
        
        # Build DataFrame
        df_probs = pd.DataFrame({
            "Emotion": [e.title() for e in probs.keys()],
            "Probability (%)": list(probs.values())
        }).set_index("Emotion")
        
        st.bar_chart(df_probs)