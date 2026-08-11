import streamlit as st

from components.layout import page_header


# ============================================================
# HEADER
# ============================================================

page_header(
    "ℹ️ About the Project",
    "System Capacity & Care Load Analytics — an end-to-end analytics and machine learning platform."
)


# ============================================================
# PROJECT OVERVIEW
# ============================================================

st.markdown("## 🎯 Project Overview")

st.markdown(
    """
    **System Capacity & Care Load Analytics** is an analytical and
    machine learning platform designed to understand historical system
    activity, monitor operational capacity, identify relationships between
    operational variables, and forecast future care-load requirements.

    The platform combines **data engineering, exploratory analytics,
    statistical forecasting, and machine learning** into a single
    interactive Streamlit application.
    """
)


# ============================================================
# BUSINESS OBJECTIVE
# ============================================================

st.markdown("## 💡 Business Objective")

st.markdown(
    """
    The primary objective of this project is to transform historical
    operational data into actionable intelligence for capacity planning
    and care-load monitoring.

    The platform helps answer questions such as:

    - How is system activity changing over time?
    - What is the current level of operational pressure?
    - How are transfers and discharges changing?
    - What does the recent trend indicate about future capacity?
    - Which operational variables are most strongly associated with
      changes in care load?
    - Can historical patterns be used to support future planning?
    """
)


# ============================================================
# DATA
# ============================================================

st.markdown("## 📊 Data & Analytics")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        ### 📂 Data Source

        **HHS Open Data**

        The project uses historical operational observations covering
        system activity, CBP custody, HHS care, transfers and discharges.

        The data is transformed through preprocessing and feature
        engineering before being used by the analytical and machine
        learning layers.
        """
    )


with col2:

    st.markdown(
        """
        ### 🧮 Feature Engineering

        The analytical dataset includes operational and temporal
        features such as:

        - Lag variables
        - Rolling averages
        - Rolling standard deviation
        - Rolling minimum / maximum
        - Daily change
        - Percentage change
        - Transfer efficiency
        - Discharge ratio
        - Occupancy pressure
        - Seasonal indicators
        """
    )


# ============================================================
# ANALYTICS PIPELINE
# ============================================================

st.markdown("## 🔄 Analytics Pipeline")

st.markdown(
    """
    The project follows an end-to-end analytical workflow:
    """
)

pipeline = [
    ("1️⃣", "Raw Data", "Historical operational data"),
    ("2️⃣", "Data Cleaning", "Missing values, formatting and validation"),
    ("3️⃣", "Feature Engineering", "Lag, rolling and operational features"),
    ("4️⃣", "Exploratory Analysis", "Trends, relationships and distributions"),
    ("5️⃣", "Forecasting", "Historical trend-based forecasting"),
    ("6️⃣", "Machine Learning", "Random Forest predictive analysis"),
    ("7️⃣", "Dashboard", "Interactive decision-support interface"),
]

for icon, title, description in pipeline:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(180deg,#111827,#0F172A);
            border:1px solid #334155;
            border-left:4px solid #2563EB;
            border-radius:12px;
            padding:14px 18px;
            margin-bottom:10px;
        ">
            <div style="font-size:17px; font-weight:600;">
                {icon} {title}
            </div>
            <div style="
                color:#94A3B8;
                margin-top:5px;
                margin-left:32px;
            ">
                {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# MACHINE LEARNING
# ============================================================

st.markdown("## 🤖 Machine Learning")

st.markdown(
    """
    The machine learning layer uses a **Random Forest regression model**
    to identify relationships between engineered operational variables
    and care-load levels.

    The model is evaluated using a chronological holdout strategy so
    that historical observations are used for training and later
    observations are reserved for evaluation.

    ### Model Performance

    - **MAE:** 79.61
    - **RMSE:** 101.52
    - **R² Score:** 0.985

    The model performance indicates a strong relationship between the
    engineered operational features and the target care-load variable.
    """
)


# ============================================================
# FORECASTING
# ============================================================

st.markdown("## 🔮 Forecasting")

st.markdown(
    """
    The forecasting module uses recent historical observations to
    estimate the underlying operational trend and project it forward
    across the selected forecast horizon.

    Forecast results include:

    - Historical observations
    - Forecast values
    - Lower confidence boundary
    - Upper confidence boundary
    - Expected change
    - Percentage change

    These outputs are intended to support operational planning and
    capacity monitoring.
    """
)


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.markdown("## 🛠️ Technology Stack")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:

    st.markdown(
        """
        ### 🐍 Data & ML

        - Python
        - Pandas
        - NumPy
        - Scikit-learn
        - Joblib
        """
    )


with tech_col2:

    st.markdown(
        """
        ### 📊 Visualization

        - Streamlit
        - Plotly
        - Interactive charts
        - Analytical dashboards
        """
    )


with tech_col3:

    st.markdown(
        """
        ### 🏗️ Application

        - Modular Streamlit architecture
        - Reusable components
        - Feature-engineered datasets
        - ML model pipeline
        """
    )


# ============================================================
# DASHBOARD MODULES
# ============================================================

st.markdown("## 🧭 Dashboard Modules")

modules = [
    ("📊", "Executive Dashboard",
     "High-level operational overview and system capacity indicators."),

    ("📈", "Operational Analytics",
     "Detailed analysis of system activity, transfers, discharges and care load."),

    ("🔮", "Forecasting",
     "Forward-looking estimates of future care-load requirements."),

    ("🧠", "ML Insights",
     "Feature relationships, model performance and prediction drivers."),

    ("ℹ️", "About",
     "Project architecture, methodology, technology and documentation."),
]

for icon, title, description in modules:

    st.markdown(
        f"""
        <div style="
            background:#0F172A;
            border:1px solid #334155;
            border-radius:12px;
            padding:15px 18px;
            margin-bottom:10px;
        ">
            <div style="font-size:17px; font-weight:600;">
                {icon} {title}
            </div>
            <div style="
                color:#94A3B8;
                margin-top:5px;
            ">
                {description}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# PROJECT ARCHITECTURE
# ============================================================

st.markdown("## 🏗️ Project Architecture")

st.code(
    """
System Capacity & Care Load Analytics
│
├── Raw Data
│
├── Data Processing
│   ├── Cleaning
│   ├── Validation
│   └── EDA
│
├── Feature Engineering
│   ├── Lag Features
│   ├── Rolling Statistics
│   ├── Operational Ratios
│   └── Seasonal Features
│
├── Analytics
│   ├── Executive Dashboard
│   └── Operational Analytics
│
├── Forecasting
│   └── Trend-based Forecast
│
├── Machine Learning
│   └── Random Forest
│
└── Streamlit Application
    ├── Executive Dashboard
    ├── Operational Analytics
    ├── Forecasting
    ├── ML Insights
    └── About
    """,
    language="text"
)


# ============================================================
# IMPORTANT NOTE
# ============================================================

st.markdown("## ⚠️ Important Note")

st.info(
    """
    This platform is designed as a **decision-support and analytical
    system**. Forecasts and machine learning outputs should be
    interpreted alongside operational context and should not be treated
    as standalone operational decisions.
    """
)


# ============================================================
# PROJECT INFORMATION
# ============================================================

st.markdown("## 👨‍💻 Project Information")

info_col1, info_col2 = st.columns(2)

with info_col1:

    st.markdown(
        """
        **Project:**  
        System Capacity & Care Load Analytics

        **Data Source:**  
        HHS Open Data

        **Application:**  
        Streamlit

        **Model:**  
        Random Forest Regression
        """
    )


with info_col2:

    st.markdown(
        """
        **Version:**  
        1.0.0

        **Developer:**  
        Swimmy Sahaniya

        **Focus:**  
        Operational Analytics & Machine Learning

        **Purpose:**  
        Capacity Planning & Care-Load Intelligence
        """
    )


# ============================================================
# FOOTER
# ============================================================
st.markdown(
    """
    <hr style="margin-top:40px;">

    <div style="
    text-align:center;
    color:#94A3B8;
    font-size:13px;
    padding-bottom:10px;
    ">

    <b>System Capacity & Care Load Analytics</b><br>

    Version 1.0 • Developed by <b>Swimmy Sahaniya</b>

    </div>
    """,
    unsafe_allow_html=True
)
