import streamlit as st

from components.sidebar import render_sidebar
from components.styles import load_css


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="System Capacity & Care Load Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


# =========================================================
# GLOBAL CSS
# =========================================================

load_css()


# =========================================================
# PAGE DEFINITIONS
# =========================================================

pages = {
    "Dashboard": [
        st.Page(
            "pages/1_Executive_Dashboard.py",
            title="Executive Dashboard",
            icon="📊",
        ),
        st.Page(
            "pages/2_Operational_Analytics.py",
            title="Operational Analytics",
            icon="📈",
        ),
        st.Page(
            "pages/3_Forecasting.py",
            title="Forecasting",
            icon="🔮",
        ),
        st.Page(
            "pages/4_ML_Insights.py",
            title="ML Insights",
            icon="🤖",
        ),
        st.Page(
            "pages/5_About.py",
            title="About",
            icon="ℹ️",
        ),
    ]
}


# =========================================================
# NAVIGATION
# =========================================================

pg = st.navigation(pages)


# =========================================================
# GLOBAL SIDEBAR
# =========================================================

render_sidebar()


# =========================================================
# RUN SELECTED PAGE
# =========================================================

pg.run()
