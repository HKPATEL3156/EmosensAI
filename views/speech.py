import time
import streamlit as st
from pathlib import Path
import pandas as pd

from streamlit_webrtc import WebRtcMode, webrtc_streamer

from services.livespeech import LiveSpeech
from services.speech_service import predict_speech


def speech():
    st.title("🔊 Speech Emotion Detection")
    st.caption("Analyze vocal characteristics and emotions using audio upload or live microphone.")

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    left, right = st.columns([1.0, 1.0], gap="large")

    with left:
        st.subheader("🎵 Audio Upload")
        st.caption("Upload a short audio clip (WAV or MP3) for one-shot emotion prediction.")

        audio = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

        if audio:
            st.audio(audio)

            if st.button("Predict Emotion", width="stretch", key="predict_speech_btn"):
                temp = Path("temp_audio.wav")
                with open(temp, "wb") as f:
                    f.write(audio.read())

                with st.spinner("Analyzing vocal features..."):
                    emo, conf, probs = predict_speech(temp, return_all=True)
                    st.session_state["speech_emo"] = emo
                    st.session_state["speech_conf"] = conf
                    st.session_state["speech_probs"] = probs

                temp.unlink()
        else:
            st.info("Upload an audio file to begin.")

    with right:
        st.subheader("🎙️ Live Detection")
        st.caption("Click START, speak naturally, and the model will update continuously.")

        ctx = webrtc_streamer(
            key="speech-live",
            mode=WebRtcMode.SENDONLY,
            audio_processor_factory=LiveSpeech,
            media_stream_constraints={"audio": True, "video": False},
            async_processing=True,
        )

        if ctx.state.playing:
            st.success("Listening live...")

            live_placeholder = st.empty()

            while ctx.state.playing:
                if ctx.audio_processor:
                    emo = ctx.audio_processor.emo
                    conf = ctx.audio_processor.conf

                    st.session_state["speech_emo"] = emo
                    st.session_state["speech_conf"] = conf
                    # Clear previous upload probabilities during live streaming
                    if "speech_probs" in st.session_state:
                        del st.session_state["speech_probs"]

                    with live_placeholder.container():
                        st.markdown(
                            f"""
                            <div class='card'>
                                <h3>Live Result</h3>
                                <p><b>Emotion:</b> {emo.title() if emo != "--" else "Listening..."}</p>
                                <p><b>Confidence:</b> {conf:.2f}%</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
                time.sleep(0.5)
        else:
            st.info("Click START to begin live detection.")

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    # ---------------- Results ---------------- #
    st.subheader("🔮 Prediction Results")

    emo = st.session_state.get("speech_emo", "--")
    conf = st.session_state.get("speech_conf", 0.0)
    probs = st.session_state.get("speech_probs", None)

    emoji_map = {
        "angry": "😡",
        "disgust": "🤢",
        "fear": "😨",
        "happy": "😊",
        "neutral": "😐",
        "pleasant_surprise": "😲",
        "sad": "😢"
    }

    status = "Ready" if emo != "--" else "Waiting"

    c1, c2, c3 = st.columns(3)
    c1.metric("Emotion", f"{emoji_map.get(emo, '')} {emo.replace('_', ' ').title()}" if emo != "--" else "--")
    c2.metric("Confidence", f"{conf:.2f}%" if emo != "--" else "--")
    c3.metric("Status", status)

    # Display probabilities chart if available
    if probs:
        st.markdown("<br>", unsafe_allow_html=True)
        st.write("📊 **Emotion Probability Distribution**")
        
        # Build DataFrame
        df_probs = pd.DataFrame({
            "Emotion": [e.replace('_', ' ').title() for e in probs.keys()],
            "Probability (%)": list(probs.values())
        }).set_index("Emotion")
        
        st.bar_chart(df_probs)
