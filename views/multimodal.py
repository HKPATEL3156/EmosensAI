import streamlit as st
from pathlib import Path
import numpy as np
import cv2
from PIL import Image
import pandas as pd

from services.face_service import predict_face, extract_face
from services.speech_service import predict_speech


def multimodal():
    st.title("🔮 Multimodal Emotion Fusion")
    st.caption(
        "Combine Facial Expression and Speech analysis for a robust, multi-sensory emotion prediction."
    )

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    # Sidebar / Page settings for Weights
    st.sidebar.markdown("### Fusion Settings")
    w_face = st.sidebar.slider(
        "Face Model Weight (%)",
        min_value=0,
        max_value=100,
        value=50,
        step=5,
        help="Adjust how much influence the facial expression model has on the final prediction."
    ) / 100.0
    w_speech = 1.0 - w_face

    st.sidebar.markdown(
        f"""
        **Weight Distribution:**
        - 👤 Face: `{w_face * 100:.0f}%`
        - 🔊 Speech: `{w_speech * 100:.0f}%`
        """
    )

    left, right = st.columns(2, gap="large")

    face_img = None
    img_cv = None

    with left:
        st.subheader("👤 Step 1: Facial Input")
        face_image_file = st.file_uploader(
            "Choose a face image",
            type=["jpg", "jpeg", "png"],
            key="multi_face"
        )

        if face_image_file:
            pic = Image.open(face_image_file)
            img_np = np.array(pic)
            img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Detect face
            face_img, bbox = extract_face(img_cv)

            if face_img is not None:
                x, y, w, h = bbox
                annotated_img = img_cv.copy()
                cv2.rectangle(
                    annotated_img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    4
                )
                display_img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
                st.image(display_img, width="stretch", caption="Face Detected!")
            else:
                st.image(pic, width="stretch")
                st.warning("No face detected. The model will analyze the entire image.")
        else:
            st.info("Upload an image containing a face.")

    with right:
        st.subheader("🔊 Step 2: Speech Input")
        speech_audio_file = st.file_uploader(
            "Choose a speech audio file",
            type=["wav", "mp3"],
            key="multi_speech"
        )

        if speech_audio_file:
            st.audio(speech_audio_file)
            st.success("Speech audio uploaded successfully.")
        else:
            st.info("Upload an audio file containing speech.")

    st.markdown("<br>", unsafe_allow_html=True)

    # Prediction Trigger
    can_predict = face_image_file is not None and speech_audio_file is not None

    if st.button("Run Multimodal Fusion", width="stretch", disabled=not can_predict):
        with st.spinner("Processing both modalities..."):
            # 1. Process Face (using cropped face if available, else full image)
            target_face_img = face_img if face_img is not None else img_cv
            face_emo, face_conf, face_probs = predict_face(target_face_img, return_all=True)

            # 2. Process Speech
            temp_path = Path("temp_multi_audio.wav")
            with open(temp_path, "wb") as f:
                f.write(speech_audio_file.read())

            try:
                speech_emo, speech_conf, speech_probs = predict_speech(temp_path, return_all=True)
            finally:
                if temp_path.exists():
                    temp_path.unlink()

            # Map speech's pleasant_surprise to surprise
            if "pleasant_surprise" in speech_probs:
                speech_probs["surprise"] = speech_probs.pop("pleasant_surprise")

            # Harmonize classes
            emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
            
            # Ensure all emotions exist in both dicts
            for emo in emotions:
                if emo not in face_probs:
                    face_probs[emo] = 0.0
                if emo not in speech_probs:
                    speech_probs[emo] = 0.0

            # Calculate fused probabilities
            fused_probs = {}
            for emo in emotions:
                fused_probs[emo] = (w_face * face_probs[emo]) + (w_speech * speech_probs[emo])

            # Get final prediction
            final_emo = max(fused_probs, key=fused_probs.get)
            final_conf = fused_probs[final_emo]

            # Save results to session state
            st.session_state["multi_results"] = {
                "face_emo": face_emo,
                "face_conf": face_conf,
                "face_probs": face_probs,
                "speech_emo": speech_emo,
                "speech_conf": speech_conf,
                "speech_probs": speech_probs,
                "fused_probs": fused_probs,
                "final_emo": final_emo,
                "final_conf": final_conf,
            }

    # Display Results if available
    results = st.session_state.get("multi_results", None)

    if results:
        st.markdown("<div class='line'></div>", unsafe_allow_html=True)
        st.subheader("🔮 Fusion Results")

        # Layout for summary
        c1, c2, c3 = st.columns(3)
        
        # Determine emoji based on emotion
        emoji_map = {
            "angry": "😡",
            "disgust": "🤢",
            "fear": "😨",
            "happy": "😊",
            "neutral": "😐",
            "sad": "😢",
            "surprise": "😲"
        }
        
        final_emo = results["final_emo"]
        final_emoji = emoji_map.get(final_emo, "🧠")

        with c1:
            st.markdown(
                f"""
                <div class='card' style='border-color: #2563eb;'>
                    <h4>👤 Face Model Prediction</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>
                        {emoji_map.get(results["face_emo"], "")} {results["face_emo"].title()}
                    </p>
                    <p style='color: #94a3b8;'>Confidence: {results["face_conf"]:.2f}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c2:
            st.markdown(
                f"""
                <div class='card' style='border-color: #7c3aed;'>
                    <h4>🔊 Speech Model Prediction</h4>
                    <p style='font-size: 24px; font-weight: bold; margin: 5px 0;'>
                        {emoji_map.get(results["speech_emo"], "")} {results["speech_emo"].title()}
                    </p>
                    <p style='color: #94a3b8;'>Confidence: {results["speech_conf"]:.2f}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with c3:
            st.markdown(
                f"""
                <div class='card' style='background: linear-gradient(135deg, #1e3a8a, #4c1d95); border: none;'>
                    <h4 style='color: white;'>🔮 Fused Multimodal Emotion</h4>
                    <p style='font-size: 28px; font-weight: bold; color: white; margin: 5px 0;'>
                        {final_emoji} {final_emo.title()}
                    </p>
                    <p style='color: #cbd5e1;'>Combined Confidence: {results["final_conf"]:.2f}%</p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("📊 Probability Distribution Comparison")

        # Build a DataFrame for comparison
        emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
        chart_data = pd.DataFrame({
            "Emotion": [e.title() for e in emotions],
            "Face Model (%)": [results["face_probs"][e] for e in emotions],
            "Speech Model (%)": [results["speech_probs"][e] for e in emotions],
            "Fused Prediction (%)": [results["fused_probs"][e] for e in emotions]
        })
        
        chart_data = chart_data.set_index("Emotion")
        
        # Display bar chart
        st.bar_chart(chart_data)
        
        # Display as a clean table
        st.dataframe(
            chart_data.style.format("{:.2f}%").background_gradient(cmap="Blues"),
            width="stretch"
        )