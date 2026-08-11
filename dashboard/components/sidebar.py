import streamlit as st
from datetime import datetime


def render_sidebar():

    with st.sidebar:

        st.markdown("# app")

        # ============================
        # NAVIGATION
        # ============================

        st.page_link(
            "pages/1_Executive_Dashboard.py",
            label="Executive Dashboard",
            icon="📊"
        )

        st.page_link(
            "pages/2_Operational_Analytics.py",
            label="Operational Analytics",
            icon="📈"
        )

        st.page_link(
            "pages/3_Forecasting.py",
            label="Forecasting",
            icon="🔮"
        )

        st.page_link(
            "pages/4_ML_Insights.py",
            label="ML Insights",
            icon="🧠"
        )

        st.page_link(
            "pages/5_About.py",
            label="About",
            icon="ℹ️"
        )

        st.divider()

        # =================================================
        # SYSTEM STATUS
        # =================================================

        st.markdown(
            """
            <div style="
                background: linear-gradient(180deg,#111827,#0F172A);
                border:1px solid #334155;
                border-top:4px solid #2563EB;
                border-radius:18px;
                padding:20px;
                margin-top:20px;
            ">

            <h4 style="margin-bottom:0px;">
            SYSTEM STATUS
            </h4>

            <p style="
                padding-top:10px;
                color:#00C853;
                margin-bottom:0;
            ">
            All Systems Operational
            </p>

            <hr style="
                border:0.5px solid #2D3748;
                margin:10px 0;
            ">

            <div style="margin-bottom:10px;">
            <b>🟢 Data Pipeline</b><br>
            <p style="padding-left:20px;">Healthy</p>
            </div>

            <div style="margin-bottom:10px;">
            <b>🟢 Model Status</b><br>
            <p style="padding-left:20px;">Ready</p>
            </div>

            <div style="margin-bottom:10px;">
            <b>🟢 Data Quality</b><br>
            <p style="padding-left:20px;">Excellent</p>
            </div>

            <div>
            <b>🟢 Forecast Confidence</b><br>
            <p style="padding-left:20px;">Available</p>
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        # =================================================
        # PROJECT INFORMATION
        # =================================================

        today = datetime.now().strftime(
            "%d %b %Y, %I:%M %p"
        )

        st.markdown(
            f"""
            <div style="
                background: linear-gradient(180deg,#111827,#0F172A);
                border:1px solid #334155;
                border-top:4px solid #2563EB;
                border-radius:18px;
                padding:20px;
                margin-top:30px;
            ">

            <h4>
            📊 SYSTEM CAPACITY & CARE LOAD ANALYTICS
            </h4>

            <hr style="
                border:0.5px solid #2D3748;
                margin:10px 0;
            ">

            <div>
            <b>📅 Last Updated</b><br>
            <p style="padding-left:20px;">
            {today}
            </p>
            </div>

            <div>
            <b>📂 Data Source</b><br>
            <p style="padding-left:20px;">
            HHS Open Data
            </p>
            </div>

            <div>
            <b>👨‍💻 Developer</b><br>
            <p style="padding-left:20px;">
            Swimmy Sahaniya
            </p>
            </div>

            <div>
            <b>🟢 Version</b><br>
            <p style="padding-left:20px;">
            1.0.0
            </p>
            </div>

            </div>
            """,
            unsafe_allow_html=True
        )