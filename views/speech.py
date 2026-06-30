import streamlit as st
from pathlib import Path

from streamlit_webrtc import WebRtcMode, webrtc_streamer

from services.livespeech import LiveSpeech
from services.speech_service import predict_speech


def speech():
    st.title("Speech Emotion Detection")
    st.caption("Live microphone analysis with a lightweight speech emotion model.")

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    left, right = st.columns([1.0, 1.0], gap="large")

    with left:
        st.subheader("Audio Upload")
        st.caption("Upload a short audio clip for one-shot emotion prediction.")

        audio = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

        if audio:
            st.audio(audio)

            if st.button("Predict Emotion", use_container_width=True):
                temp = Path("temp_audio.wav")
                with open(temp, "wb") as f:
                    f.write(audio.read())

                emo, conf = predict_speech(temp)
                st.session_state["speech_emo"] = emo
                st.session_state["speech_conf"] = conf

                temp.unlink()
        else:
            st.info("Upload an audio file to begin.")

    with right:
        st.subheader("Live Detection")
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

            if ctx.audio_processor:
                emo = ctx.audio_processor.emo
                conf = ctx.audio_processor.conf

                st.session_state["speech_emo"] = emo
                st.session_state["speech_conf"] = conf

                st.markdown(
                    f"""
                    <div class='card'>
                        <h3>Live Result</h3>
                        <p><b>Emotion:</b> {emo.title()}</p>
                        <p><b>Confidence:</b> {conf:.2f}%</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("Click START to begin live detection.")

    st.markdown("<div class='line'></div>", unsafe_allow_html=True)

    st.subheader("Prediction Result")

    emo = st.session_state.get("speech_emo", "--")
    conf = st.session_state.get("speech_conf", 0.0)
    status = "Waiting"

    if emo != "--":
        status = "Ready"

    c1, c2, c3 = st.columns(3)
    c1.metric("Emotion", emo.title() if emo != "--" else "--")
    c2.metric("Confidence", f"{conf:.2f}%" if emo != "--" else "--")
    c3.metric("Status", status)
