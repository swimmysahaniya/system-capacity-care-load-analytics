import streamlit as st


def load_css():
    st.markdown("""
    <style>

    .main {
        background-color: #F8FAFC;
    }

    h1, h2, h3 {
        color: #2563EB;
        font-weight: 700;
    }

    div[data-testid="metric-container"] {
        background: white;
        border-radius: 15px;
        padding: 18px;
        box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #E5E7EB;
    }

    section[data-testid="stSidebar"] {
        background-color: #1E293B;
    }

    section[data-testid="stSidebar"] * {
        color: white;
    }

    hr {
        margin-top: 10px;
        margin-bottom: 20px;
    }

    </style>
    """, unsafe_allow_html=True)

