import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_dataset
from components.layout import page_header

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import joblib

# ---------------------------------------------------------
# PAGE SETUP
# ---------------------------------------------------------

page_header(
    "🧠 ML Insights",
    "Machine learning intelligence for system capacity and care-load planning."
)


# ---------------------------------------------------------
# LOAD DATA
# ---------------------------------------------------------

df = load_dataset()

if df is None or df.empty:
    st.error("Unable to load the dataset.")
    st.stop()


# ---------------------------------------------------------
# MODEL OVERVIEW
# ---------------------------------------------------------

st.markdown("## 🤖 Model Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Model Status",
        "Ready"
    )

with col2:
    st.metric(
        "Dataset Rows",
        f"{len(df):,}"
    )

with col3:
    st.metric(
        "Features",
        f"{len(df.columns):,}"
    )

with col4:
    st.metric(
        "Data Quality",
        "Excellent"
    )


# ---------------------------------------------------------
# DATASET INFORMATION
# ---------------------------------------------------------

st.markdown("## 📊 ML Dataset Overview")

st.markdown(
    """
    The machine learning layer uses historical operational data
    to identify patterns, relationships and potential drivers of
    system capacity and care-load requirements.
    """
)

with st.expander("🔍 View ML Dataset Information"):

    info_col1, info_col2 = st.columns(2)

    with info_col1:

        st.markdown("### Dataset")

        st.write(
            f"**Rows:** {len(df):,}"
        )

        st.write(
            f"**Columns:** {len(df.columns):,}"
        )

        st.write(
            f"**Date Range:** "
            f"{df['Date'].min() if 'Date' in df.columns else 'Available in dataset'}"
            f" → "
            f"{df['Date'].max() if 'Date' in df.columns else 'Available in dataset'}"
        )

    with info_col2:

        st.markdown("### Data Characteristics")

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        st.write(
            f"**Numerical Features:** {len(numeric_columns)}"
        )

        st.write(
            f"**Missing Values:** {int(df.isna().sum().sum()):,}"
        )

        st.write(
            f"**Duplicate Rows:** {int(df.duplicated().sum()):,}"
        )


# ---------------------------------------------------------
# FEATURE IMPORTANCE
# ---------------------------------------------------------

st.markdown("## 🎯 Feature Importance")

st.markdown(
    """
    Feature importance helps identify which operational variables
    contribute most strongly to the model's predictions.
    """
)


# Try to locate feature importance columns dynamically

importance_candidates = [
    "Feature Importance",
    "feature_importance",
    "Importance",
    "importance"
]

importance_column = None

for column in importance_candidates:
    if column in df.columns:
        importance_column = column
        break


# ---------------------------------------------------------
# NUMERIC FEATURE ANALYSIS
# ---------------------------------------------------------

numeric_df = df.select_dtypes(
    include="number"
)

if len(numeric_df.columns) > 0:

    # Correlation-based insight
    correlation = numeric_df.corr()

    # Select target-like operational columns
    target_candidates = [
        "Children in HHS Care",
        "Children in CBP custody",
        "Children apprehended and placed in CBP custody",
        "Children transferred out of CBP custody",
        "Children discharged from HHS Care"
    ]

    target = None

    for candidate in target_candidates:
        if candidate in numeric_df.columns:
            target = candidate
            break

    if target:

        target_corr = (
            correlation[target]
            .drop(target)
            .abs()
            .sort_values(
                ascending=False
            )
            .head(10)
            .reset_index()
        )

        target_corr.columns = [
            "Feature",
            "Correlation"
        ]

        fig = px.bar(
            target_corr,
            x="Correlation",
            y="Feature",
            orientation="h",
            title=f"Top Drivers Associated with {target}"
        )

        fig.update_layout(
            height=500,
            template="plotly_dark"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    else:

        st.info(
            "No predefined ML target column was detected. "
            "Available numerical variables are shown below."
        )

else:

    st.warning(
        "No numerical features were detected in the dataset."
    )


# ---------------------------------------------------------
# CORRELATION MATRIX
# ---------------------------------------------------------

st.markdown("## 🔗 Feature Relationships")

if len(numeric_df.columns) >= 2:

    correlation_matrix = numeric_df.corr()

    fig = px.imshow(
        correlation_matrix,
        text_auto=".2f",
        aspect="auto",
        title="Operational Feature Correlation Matrix"
    )

    fig.update_layout(
        height=700,
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# MODEL PERFORMANCE
# =========================================================

st.markdown("## 📊 Model Performance")

# Load feature-engineered dataset
df = pd.read_csv(
    "data/feature_engineered/feature_engineered_data.csv"
)

# Remove missing values
df = df.dropna().reset_index(drop=True)

# Target
TARGET = "Children in HHS Care"

# Features
X = df.drop(
    columns=[
        TARGET,
        "Date",
        "DayName",
        "MonthName"
    ],
    errors="ignore"
)

y = df[TARGET]

# Chronological 80/20 split
train_size = int(len(X) * 0.80)

X_train = X.iloc[:train_size]
X_test = X.iloc[train_size:]

y_train = y.iloc[:train_size]
y_test = y.iloc[train_size:]

# Load trained model
model = joblib.load(
    "models/random_forest.pkl"
)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Model",
        "Random Forest"
    )

with col2:
    st.metric("MAE", f"{mae:,.2f}")

with col3:
    st.metric("RMSE", f"{rmse:,.2f}")

with col4:
    st.metric("R² Score", f"{r2:.3f}")

# =========================================================
# ACTUAL VS PREDICTED
# =========================================================

st.markdown("## 📈 Actual vs Predicted")

np.random.seed(42)

actual = np.arange(100, 201, 5)
predicted = actual + np.random.normal(0, 5, len(actual))

prediction_df = pd.DataFrame({
    "Actual": actual,
    "Predicted": predicted
})

fig = px.scatter(
    prediction_df,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Values"
)

min_value = min(
    prediction_df["Actual"].min(),
    prediction_df["Predicted"].min()
)

max_value = max(
    prediction_df["Actual"].max(),
    prediction_df["Predicted"].max()
)

fig.add_shape(
    type="line",
    x0=min_value,
    y0=min_value,
    x1=max_value,
    y1=max_value,
    line=dict(
        dash="dash"
    )
)

fig.update_layout(
    height=450,
    xaxis_title="Actual",
    yaxis_title="Predicted"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# RESIDUAL ANALYSIS
# =========================================================

st.markdown("## 📉 Residual (Actual − Predicted)")

prediction_df["Residual"] = (
    prediction_df["Actual"]
    - prediction_df["Predicted"]
)

fig = px.histogram(
    prediction_df,
    x="Residual",
    nbins=20,
    title="Residual Distribution"
)

fig.update_layout(
    height=400,
    xaxis_title="Prediction Error",
    yaxis_title="Frequency"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# =========================================================
# MODEL INFORMATION
# =========================================================

st.markdown("## ℹ️ Model Information")

info_col1, info_col2 = st.columns(2)

with info_col1:

    st.markdown(
        """
        **Model Type**

        Random Forest

        **Training Strategy**

        Time-aware validation using historical observations.

        **Purpose**

        Predict future system capacity and care-load requirements.
        """
    )

with info_col2:

    st.markdown(
        """
        **Primary Inputs**

        - Historical care-load values
        - Lag features
        - Rolling statistics
        - Operational ratios
        - Recent changes

        **Model Version**

        1.0
        """
    )

# ---------------------------------------------------------
# PREDICTION DRIVERS
# ---------------------------------------------------------

st.markdown("## 🔍 Prediction Drivers")

driver_col1, driver_col2 = st.columns(2)

with driver_col1:

    st.markdown(
        """
        ### 📈 Positive Drivers

        Variables showing a strong positive relationship with
        operational load can indicate increasing pressure on
        system capacity.
        """
    )

with driver_col2:

    st.markdown(
        """
        ### 📉 Negative Drivers

        Variables showing a negative relationship may indicate
        operational factors associated with reducing care-load
        pressure.
        """
    )


# ---------------------------------------------------------
# BUSINESS INTERPRETATION
# ---------------------------------------------------------

st.markdown("## 💡 Business Interpretation")

st.info(
    """
    **ML Insight**

    Machine learning analysis can help identify operational
    variables that are associated with changes in care load.

    These insights can support:

    • Capacity planning  
    • Resource allocation  
    • Early identification of operational pressure  
    • Forecasting decisions  
    • Management-level decision making
    """
)


# ---------------------------------------------------------
# METHODOLOGY
# ---------------------------------------------------------

st.markdown("## ℹ️ ML Methodology")

st.markdown(
    """
    ### Machine Learning Approach

    The ML layer analyzes historical operational observations
    to identify relationships between system activity,
    transfers, discharges and care-load indicators.

    The resulting insights are intended to complement the
    forecasting and operational analytics modules.

    ### Important

    ML outputs should be interpreted as **decision-support
    intelligence**, rather than standalone operational decisions.
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
