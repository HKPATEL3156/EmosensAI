import streamlit as st


def set_theme():

    st.markdown("""
    <style>

    # #MainMenu{
    # visibility:hidden;
    # }

    # footer{
    # visibility:hidden;
    # }

    # header{
    # visibility:hidden;
    # }

    .block-container{
    max-width:1300px;
    padding-top:2rem;
    padding-bottom:2rem;
    }

    section[data-testid="stSidebar"]{
    background:#0f172a;
    border-right:1px solid #1e293b;
    }

    section[data-testid="stSidebar"] *{
    color:white;
    }

    div[data-testid="stMetric"]{
    background:#18181b;
    border:1px solid #2a2a2a;
    border-radius:15px;
    padding:18px;
    text-align:center;
    }

    .hero{
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    border-radius:22px;
    padding:50px;
    margin-bottom:25px;
    }

    .hero-title{
    font-size:55px;
    font-weight:700;
    color:white;
    margin-bottom:10px;
    }

    .hero-sub{
    font-size:22px;
    color:white;
    margin-bottom:25px;
    }

    .hero-text{
    font-size:18px;
    line-height:1.8;
    color:white;
    max-width:900px;
    }

    .card{
    background:#18181b;
    border:1px solid #2a2a2a;
    border-radius:18px;
    padding:25px;
    height:100%;
    }

    .card-title{
    font-size:28px;
    font-weight:600;
    margin-bottom:20px;
    color:white;
    }

    .card-text{
    font-size:17px;
    line-height:1.8;
    color:#d1d5db;
    }

    .sec-title{
    font-size:36px;
    font-weight:700;
    margin-top:15px;
    margin-bottom:20px;
    }

    .line{
    height:3px;
    background:linear-gradient(to right,#2563eb,#7c3aed);
    border-radius:20px;
    margin:30px 0;
    }

    .stButton>button{

    width:100%;

    height:48px;

    border:none;

    border-radius:10px;

    background:linear-gradient(135deg,#2563eb,#7c3aed);

    color:white;

    font-weight:600;

    font-size:16px;

    transition:0.3s;

    }

    .stButton>button:hover{

    transform:translateY(-2px);

    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: #090d16 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    section[data-testid="stSidebar"] hr {
        border: 0 !important;
        height: 1px !important;
        background: rgba(255, 255, 255, 0.06) !important;
        margin: 20px 0 !important;
    }

    /* Custom navigation menu - Flat SaaS Style */
    div[role="radiogroup"] {
        display: flex !important;
        flex-direction: column !important;
        gap: 4px !important;
        padding: 0 !important;
    }

    div[role="radiogroup"] > label {
        background: transparent !important;
        border: 1px solid transparent !important;
        border-radius: 8px !important;
        padding: 10px 14px !important;
        color: #94a3b8 !important;
        font-weight: 500 !important;
        font-size: 14.5px !important;
        transition: all 0.15s ease !important;
        cursor: pointer !important;
        width: 100% !important;
    }

    div[role="radiogroup"] > label:hover {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #f1f5f9 !important;
        transform: none !important;
    }

    /* Selected state - Flat SaaS Style */
    div[role="radiogroup"] > label:has(input:checked) {
        background: rgba(255, 255, 255, 0.08) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        color: white !important;
        font-weight: 600 !important;
        box-shadow: none !important;
        transform: none !important;
    }

    /* Hide default radio circle */
    div[role="radiogroup"] > label > div:first-child {
        display: none !important;
    }
    
    /* Fix text color inside selected radio */
    div[role="radiogroup"] > label:has(input:checked) div {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)