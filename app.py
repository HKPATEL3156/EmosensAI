import streamlit as st

from utils import set_theme

from views.home import home
from views.speech import speech
from views.multimodal import multimodal

try:
    from views.face import face
except Exception:
    def face():
        st.error("Face emotion is unavailable in this environment because TensorFlow is not compatible here.")

st.set_page_config(
    page_title="EmoSens AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

set_theme()

# Sidebar
with st.sidebar:

    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 10px; padding: 10px 0;">
            <h1 style="font-size: 28px; font-weight: 800; background: linear-gradient(135deg, #3b82f6, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; display: inline-block;">🧠 EmoSens AI</h1>
            <p style="color: #94a3b8; font-size: 13.5px; line-height: 1.5; margin: 8px 0 0 0;">
                Multimodal Emotion Detection<br>
                using Facial Expressions and Speech
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### Navigation")

    page = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "👤 Face Emotion",
            "🔊 Speech Emotion",
            "🔮 Multimodal Fusion"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption("Version 1.0")


# Routing
if "Home" in page:
    home()

elif "Face" in page:
    face()

elif "Speech" in page:
    speech()

else:
    multimodal()