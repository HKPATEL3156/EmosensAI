import streamlit as st


def home():
    st.markdown(
        """
        <style>
        .home-shell {
            display: flex;
            flex-direction: column;
            gap: 28px;
            padding-bottom: 28px;
        }
        .hero-card {
            background: #090d16;
            background-image: radial-gradient(rgba(99, 102, 241, 0.08) 1.5px, transparent 0);
            background-size: 24px 24px;
            border: 1px solid rgba(255, 255, 255, 0.12);
            border-radius: 24px;
            padding: 40px 45px;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
            position: relative;
            overflow: hidden;
            transition: border-color 0.3s ease;
            margin-bottom: 24px;
        }
        .hero-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(99, 102, 241, 0.25), transparent);
        }
        .hero-card:hover {
            border-color: rgba(99, 102, 241, 0.35);
        }
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 5px 12px;
            border-radius: 999px;
            background: rgba(99, 102, 241, 0.08);
            color: #818cf8;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 18px;
            border: 1px solid rgba(99, 102, 241, 0.25);
        }
        .hero-title {
            font-size: 46px;
            font-weight: 800;
            background: linear-gradient(135deg, #ffffff 0%, #cbd5e1 50%, #94a3b8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 0 0 6px 0;
            letter-spacing: -0.02em;
        }
        .hero-sub {
            font-size: 19px;
            background: linear-gradient(90deg, #60a5fa, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 12px;
            font-weight: 600;
            letter-spacing: -0.01em;
        }
        .hero-text {
            font-size: 15px;
            line-height: 1.7;
            color: #94a3b8;
            max-width: 900px;
        }
        .card {
            background: #090d16;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: border-color 0.3s ease, box-shadow 0.3s ease, transform 0.3s ease;
            margin-bottom: 24px;
        }
        .card:hover {
            border-color: rgba(99, 102, 241, 0.3);
            transform: translateY(-2px);
            box-shadow: 0 15px 35px rgba(99, 102, 241, 0.05);
        }
        .card h3 {
            color: white;
            margin: 0 0 10px 0;
            font-size: 18px;
            font-weight: 700;
            letter-spacing: -0.01em;
        }
        .card p {
            color: #94a3b8;
            margin: 0;
            font-size: 14px;
            line-height: 1.7;
        }
        .soft-card {
            background: linear-gradient(135deg, rgba(99, 102, 241, 0.04), rgba(167, 139, 250, 0.04));
            border-color: rgba(99, 102, 241, 0.25);
        }
        .soft-card:hover {
            border-color: rgba(99, 102, 241, 0.4);
        }
        .metric-card {
            background: #090d16;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 18px 20px;
            height: 95px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
            transition: border-color 0.3s ease, transform 0.3s ease;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin-bottom: 24px;
        }
        .metric-card:hover {
            border-color: rgba(99, 102, 241, 0.3);
            transform: translateY(-2px);
        }
        .module-card {
            background: #090d16;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 24px;
            height: 100%;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1), border-color 0.3s ease;
            display: flex;
            flex-direction: column;
            margin-bottom: 24px;
        }
        .module-card:hover {
            transform: translateY(-4px);
            border-color: rgba(255, 255, 255, 0.2);
        }
        .module-title {
            color: white;
            font-size: 19px;
            font-weight: 700;
            margin: 0 0 4px 0;
            letter-spacing: -0.01em;
        }
        .module-copy {
            color: #94a3b8;
            font-size: 14px;
            line-height: 1.65;
            margin-bottom: 16px;
            flex-grow: 1;
        }
        .module-label {
            color: #4b5563;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            font-weight: 700;
            margin: 12px 0 8px 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 4px;
        }
        .chip {
            display: inline-block;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid rgba(255, 255, 255, 0.15);
            color: #cbd5e1;
            padding: 4px 10px;
            border-radius: 999px;
            font-size: 11.5px;
            font-weight: 500;
            margin: 0 5px 6px 0;
        }
        .tech-chip {
            background: rgba(99, 102, 241, 0.06);
            border-color: rgba(99, 102, 241, 0.3);
            color: #a5b4fc;
        }
        .step-card {
            background: #090d16;
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 18px;
            padding: 20px;
            height: 100%;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
            transition: transform 0.3s ease, border-color 0.3s ease;
            display: flex;
            flex-direction: column;
            margin-bottom: 24px;
        }
        .step-card:hover {
            transform: translateY(-3px);
            border-color: rgba(99, 102, 241, 0.35);
        }
        .step-number {
            color: #818cf8;
            font-size: 10.5px;
            font-weight: 800;
            letter-spacing: 0.08em;
            margin-bottom: 4px;
        }
        .step-title {
            color: white;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 8px;
            letter-spacing: -0.01em;
        }
        .step-copy {
            color: #94a3b8;
            font-size: 13px;
            line-height: 1.6;
        }
        .divider {
            height: 1px;
            background: rgba(255, 255, 255, 0.05);
            margin: 15px 0 20px 0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<div class='home-shell'>", unsafe_allow_html=True)

    # Hero Section
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-badge">✨ Next-Gen Multimodal Framework</div>
            <div class="hero-title">🧠 EmoSens AI</div>
            <div class="hero-sub">Multimodal emotion detection system</div>
            <div class="hero-text">
                EmoSens AI combines facial expressions and voice cues to understand emotions more accurately.
                It is built for human-computer interaction, mental health monitoring, and sentiment analysis with a polished real-time experience.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stats / Metrics Grid
    stats = st.columns(4)
    metric_items = [
        ("👤 Face Model", "CNN (ResNet/VGG)", "#3b82f6"),
        ("🔊 Speech Model", "Wav2Vec2 (Transformer)", "#8b5cf6"),
        ("📈 Accuracy", "95%+ (TESS/FER)", "#10b981"),
        ("⚡ Processing", "Realtime / Live", "#f59e0b"),
    ]
    for col, (title, value, color) in zip(stats, metric_items):
        with col:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div style="display: flex; align-items: center; font-size: 11px; color: #6b7280; text-transform: uppercase; letter-spacing: 0.08em; font-weight: 700; margin-bottom: 6px;">
                        <span style="display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: {color}; margin-right: 8px;"></span>
                        {title}
                    </div>
                    <div style="font-size: 15px; color: white; font-weight: 600; letter-spacing: -0.01em;">{value}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    # Project Overview & Highlights
    overview_col, highlight_col = st.columns([1.2, 0.8])
    with overview_col:
        st.markdown(
            """
            <div class="card">
                <h3>🔬 Project Overview</h3>
                <p>
                    EmoSens AI uses two complementary signals—facial expressions and voice tone—to create a more reliable emotional understanding.
                    By combining both modalities with late fusion, it reduces ambiguity and improves confidence in the final prediction.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with highlight_col:
        st.markdown(
            """
            <div class="card soft-card">
                <h3>✨ Why it stands out</h3>
                <p>
                    Single-channel systems often struggle when one signal is weak or unclear. This multimodal approach balances visual and audio cues for a stronger result.
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Core Modules Header
    st.markdown(
        """
        <div style="margin: 5px 0 12px 0;">
            <div style="font-size: 22px; font-weight: 800; color: white; letter-spacing: -0.01em;">🛠️ Core Modules</div>
            <div style="font-size: 14px; color: #6b7280; margin-top: 4px;">Three specialized modules that work together to deliver trustworthy emotion recognition.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Core Modules Grid
    face_col, speech_col, fusion_col = st.columns(3)

    with face_col:
        st.markdown(
            """
            <div class="module-card" style="border-top: 2px solid #3b82f6;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom: 12px;">
                    <div>
                        <div class="module-title">👤 Facial Emotion</div>
                        <div style="font-size: 12px; color: #6b7280;">Vision-driven analysis</div>
                    </div>
                    <span class="chip" style="background: rgba(59, 130, 246, 0.08); border-color: rgba(59, 130, 246, 0.15); color: #60a5fa; margin: 0; font-size: 10px; font-weight: 700;">VISION</span>
                </div>
                <div class="module-copy">Analyzes face expressions in real time or from uploaded images and predicts emotions with strong visual context.</div>
                <div class="module-label">Technologies</div>
                <div>
                    <span class="chip tech-chip">CNN</span>
                    <span class="chip tech-chip">Haar Cascades</span>
                    <span class="chip tech-chip">OpenCV</span>
                </div>
                <div class="module-label">Supported emotions</div>
                <div>
                    <span class="chip">😡 Angry</span>
                    <span class="chip">🤢 Disgust</span>
                    <span class="chip">😨 Fear</span>
                    <span class="chip">😊 Happy</span>
                    <span class="chip">😐 Neutral</span>
                    <span class="chip">😢 Sad</span>
                    <span class="chip">😲 Surprise</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with speech_col:
        st.markdown(
            """
            <div class="module-card" style="border-top: 2px solid #8b5cf6;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom: 12px;">
                    <div>
                        <div class="module-title">🔊 Speech Emotion</div>
                        <div style="font-size: 12px; color: #6b7280;">Audio-based emotion cues</div>
                    </div>
                    <span class="chip" style="background: rgba(139, 92, 246, 0.08); border-color: rgba(139, 92, 246, 0.15); color: #a78bfa; margin: 0; font-size: 10px; font-weight: 700;">AUDIO</span>
                </div>
                <div class="module-copy">Reads vocal tone, pitch, and prosody from microphone recordings or audio files and processes them on the fly.</div>
                <div class="module-label">Technologies</div>
                <div>
                    <span class="chip tech-chip">Wav2Vec2</span>
                    <span class="chip tech-chip">Transformers</span>
                    <span class="chip tech-chip">Librosa</span>
                </div>
                <div class="module-label">Supported emotions</div>
                <div>
                    <span class="chip">😡 Angry</span>
                    <span class="chip">🤢 Disgust</span>
                    <span class="chip">😨 Fear</span>
                    <span class="chip">😊 Happy</span>
                    <span class="chip">😐 Neutral</span>
                    <span class="chip">😢 Sad</span>
                    <span class="chip">😲 Surprise</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with fusion_col:
        st.markdown(
            """
            <div class="module-card" style="border-top: 2px solid #10b981;">
                <div style="display:flex; justify-content:space-between; align-items:flex-start; gap:10px; margin-bottom: 12px;">
                    <div>
                        <div class="module-title">🔮 Multimodal Fusion</div>
                        <div style="font-size: 12px; color: #6b7280;">Hybrid decision layer</div>
                    </div>
                    <span class="chip" style="background: rgba(16, 185, 129, 0.08); border-color: rgba(16, 185, 129, 0.15); color: #34d399; margin: 0; font-size: 10px; font-weight: 700;">HYBRID</span>
                </div>
                <div class="module-copy">Combines facial and vocal cues with weighted probability fusion to create a stronger final prediction.</div>
                <div class="module-label">Fusion methods</div>
                <div>
                    <span class="chip tech-chip">Late Fusion</span>
                    <span class="chip tech-chip">Weighted Average</span>
                    <span class="chip tech-chip">Decision Fusion</span>
                </div>
                <div class="module-label">Key advantage</div>
                <div style="color: #94a3b8; font-size: 13.5px; line-height: 1.6;">
                    Reduces classification errors compared to single-channel systems.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # Workflow Section
    st.subheader("🔄 System Workflow")
    st.markdown("<div style='height: 4px;'></div>", unsafe_allow_html=True)
    
    workflow_cols = st.columns(5)
    workflow_items = [
        ("STEP 01", "📥", "Input Capture", "Upload images or audio or stream live feeds through webcam and microphone."),
        ("STEP 02", "⚙️", "Preprocessing", "Extract face crops and resample audio for consistent model input."),
        ("STEP 03", "🤖", "Inference", "Run the prepared inputs through CNN and Wav2Vec2 for emotion prediction."),
        ("STEP 04", "🔮", "Late Fusion", "Blend both predictions into one final confidence-based decision."),
        ("STEP 05", "📊", "Output", "Show the final emotion and confidence to the user in a clear view."),
    ]
    for col, (step, icon, title, copy) in zip(workflow_cols, workflow_items):
        with col:
            border_color = ["#3b82f6", "#8b5cf6", "#ec4899", "#f59e0b", "#10b981"][workflow_items.index((step, icon, title, copy))]
            st.markdown(
                f"""
                <div class="step-card" style="border-top: 2px solid {border_color};">
                    <div class="step-number">{step}</div>
                    <div style="font-size: 26px; margin: 8px 0;">{icon}</div>
                    <div class="step-title">{title}</div>
                    <div class="step-copy">{copy}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<div class='divider'></div>", unsafe_allow_html=True)

    # # Get Started Navigation
    # st.subheader("🚀 Get Started")
    # st.caption("Select a module below to launch the interactive workspace.")

    # c1, c2, c3 = st.columns(3)
    # with c1:
    #     if st.button("👤 Face Emotion Detection", width="stretch", key="go_face_btn"):
    #         st.session_state["navigation_radio"] = "👤 Face Emotion"
    #         st.rerun()
    # with c2:
    #     if st.button("🔊 Speech Emotion Detection", width="stretch", key="go_speech_btn"):
    #         st.session_state["navigation_radio"] = "🔊 Speech Emotion"
    #         st.rerun()
    # with c3:
    #     if st.button("🔮 Multimodal Emotion Fusion", width="stretch", key="go_multi_btn"):
    #         st.session_state["navigation_radio"] = "🔮 Multimodal Fusion"
    #         st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)