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

    st.markdown("# EmoSens AI")

    st.markdown(
        """
        <span style="color:#94a3b8;">
        Multimodal Emotion Detection<br>
        using Facial Expressions and Speech
        </span>
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