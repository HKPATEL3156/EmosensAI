import streamlit as st


def home():

    st.markdown("""
   <div class="hero">

   <div class="hero-title">
   EmoSense AI
   </div>

   <div class="hero-sub">
   Multimodal Emotion Detection using Facial Expressions and Speech
   </div>

   <div class="hero-text">

   Detect human emotions from facial expressions and speech using
   deep learning models through an interactive application.

   </div>

   </div>
   """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Face Model", "Ready")
    c2.metric("Speech Model", "Ready")
    c3.metric("Upload", "Available")
    c4.metric("Realtime", "Coming Soon")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">

    <h3>About Project</h3>

    <p>

    EmoSense AI is a multimodal emotion detection system developed
    using Deep Learning.

    The application predicts emotions from

    • Facial Expressions

    • Speech Signals

    and later combines both predictions for multimodal emotion analysis.

    </p>

    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Project Modules")

    c1, c2, c3 = st.columns(3)

    with c1:

        st.markdown("""
        <div class="card">

        <h3>Face Emotion</h3>

        <p>

        ✓ Image Upload

        <br><br>

        ✓ Live Camera

        <br><br>

        ✓ Emotion Prediction

        </p>

        </div>
        """, unsafe_allow_html=True)

    with c2:

        st.markdown("""
        <div class="card">

        <h3>Speech Emotion</h3>

        <p>

        ✓ Audio Upload

        <br><br>

        ✓ Live Microphone

        <br><br>

        ✓ Emotion Prediction

        </p>

        </div>
        """, unsafe_allow_html=True)

    with c3:

        st.markdown("""
        <div class="card">

        <h3>Multimodal</h3>

        <p>

        ✓ Face + Speech

        <br><br>

        ✓ Emotion Fusion

        <br><br>

        ✓ Final Prediction

        </p>

        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.subheader("Workflow")

    st.markdown("""
    <div class="card">

    Image / Camera

    <br><br>

    ↓

    <br><br>

    Face Emotion Model

    <br><br>

    +

    <br><br>

    Audio / Microphone

    <br><br>

    ↓

    <br><br>

    Speech Emotion Model

    <br><br>

    ↓

    <br><br>

    Final Emotion Prediction

    </div>
    """, unsafe_allow_html=True)