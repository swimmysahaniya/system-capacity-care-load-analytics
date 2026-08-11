import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from utils import load_dataset
from components.layout import page_header


# ============================================================
# PAGE SETUP
# ============================================================

page_header(
    "🔮 Forecasting",
    "Predictive analysis to anticipate future system capacity and care-load requirements."
)


# ============================================================
# LOAD DATA
# ============================================================

df = load_dataset()


# ============================================================
# CLEAN COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()


# ============================================================
# COLUMN DEFINITIONS
# ============================================================

DATE_COL = "Date"

HHS_COL = "Children in HHS Care"

CBP_COL = "Children in CBP custody"

TRANSFERS_COL = "Children transferred out of CBP custody"

DISCHARGES_COL = "Children discharged from HHS Care"


# ============================================================
# VALIDATE REQUIRED COLUMNS
# ============================================================

required_columns = [
    DATE_COL,
    HHS_COL,
    CBP_COL,
    TRANSFERS_COL,
    DISCHARGES_COL
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        f"Missing required columns: {missing_columns}"
    )

    st.write("Available columns:")
    st.write(df.columns.tolist())

    st.stop()


# ============================================================
# DATE PROCESSING
# ============================================================

df[DATE_COL] = pd.to_datetime(df[DATE_COL])

df = df.sort_values(DATE_COL).copy()


# ============================================================
# FORECAST CONTROLS
# ============================================================

st.markdown("## 🎯 Forecast Configuration")

col1, col2 = st.columns(2)

with col1:

    metric = st.selectbox(
        "Select Metric",
        [
            "Children in HHS Care",
            "Children in CBP custody",
            "Children transferred out of CBP custody",
            "Children discharged from HHS Care"
        ]
    )


with col2:

    forecast_days = st.selectbox(
        "Forecast Horizon",
        [7, 14, 30, 60, 90],
        index=2,
        format_func=lambda x: f"{x} days"
    )


# ============================================================
# MAP SELECTED METRIC
# ============================================================

metric_map = {
    "Children in HHS Care": HHS_COL,
    "Children in CBP custody": CBP_COL,
    "Children transferred out of CBP custody": TRANSFERS_COL,
    "Children discharged from HHS Care": DISCHARGES_COL
}

target_col = metric_map[metric]


# ============================================================
# PREPARE TIME SERIES
# ============================================================

forecast_df = df[
    [
        DATE_COL,
        target_col
    ]
].copy()

forecast_df[target_col] = pd.to_numeric(
    forecast_df[target_col],
    errors="coerce"
)

forecast_df = forecast_df.dropna()

forecast_df = forecast_df.sort_values(DATE_COL)


if len(forecast_df) < 30:

    st.warning(
        "Not enough historical observations to generate a reliable forecast."
    )

    st.stop()


# ============================================================
# FORECAST METHOD
# ============================================================

# Rolling-window linear trend.
# This gives us a transparent baseline forecast
# without introducing an external ML dependency.

window_size = min(90, len(forecast_df))

recent_df = forecast_df.tail(window_size).copy()

x = np.arange(len(recent_df))

y = recent_df[target_col].values


# Linear regression using numpy
slope, intercept = np.polyfit(x, y, 1)


# ============================================================
# FUTURE DATES
# ============================================================

last_date = forecast_df[DATE_COL].max()

future_dates = pd.date_range(
    start=last_date + pd.Timedelta(days=1),
    periods=forecast_days,
    freq="D"
)


future_x = np.arange(
    len(recent_df),
    len(recent_df) + forecast_days
)


forecast_values = (
    intercept +
    slope * future_x
)


# ============================================================
# CONFIDENCE INTERVAL
# ============================================================

predicted_history = (
    intercept +
    slope * x
)

residuals = y - predicted_history

std_error = np.std(residuals)

confidence_multiplier = 1.96

lower_bound = (
    forecast_values -
    confidence_multiplier * std_error
)

upper_bound = (
    forecast_values +
    confidence_multiplier * std_error
)


# Prevent negative operational counts

forecast_values = np.maximum(
    forecast_values,
    0
)

lower_bound = np.maximum(
    lower_bound,
    0
)

upper_bound = np.maximum(
    upper_bound,
    0
)


# ============================================================
# FORECAST DATAFRAME
# ============================================================

forecast_result = pd.DataFrame(
    {
        DATE_COL: future_dates,
        "Forecast": forecast_values,
        "Lower Bound": lower_bound,
        "Upper Bound": upper_bound
    }
)


# ============================================================
# FORECAST SUMMARY
# ============================================================

current_value = forecast_df[target_col].iloc[-1]

forecast_end_value = forecast_result["Forecast"].iloc[-1]

change = forecast_end_value - current_value

change_pct = (
    change / current_value * 100
    if current_value != 0
    else 0
)


# ============================================================
# KPI CARDS
# ============================================================

st.markdown("## 📊 Forecast Summary")

c1, c2, c3, c4 = st.columns(4)


with c1:

    st.metric(
        "Current Value",
        f"{current_value:,.0f}"
    )


with c2:

    st.metric(
        f"{forecast_days}-Day Forecast",
        f"{forecast_end_value:,.0f}"
    )


with c3:

    st.metric(
        "Expected Change",
        f"{change:+,.0f}"
    )


with c4:

    st.metric(
        "Change %",
        f"{change_pct:+.1f}%"
    )


# ============================================================
# HISTORICAL + FORECAST CHART
# ============================================================

st.markdown(
    f"## 📈 {metric} — Historical & Forecast"
)


fig = go.Figure()


# Historical data

fig.add_trace(
    go.Scatter(
        x=recent_df[DATE_COL],
        y=recent_df[target_col],
        mode="lines",
        name="Historical"
    )
)


# Forecast

fig.add_trace(
    go.Scatter(
        x=forecast_result[DATE_COL],
        y=forecast_result["Forecast"],
        mode="lines",
        name="Forecast",
        line=dict(
            dash="dash"
        )
    )
)


# Confidence interval

fig.add_trace(
    go.Scatter(
        x=list(forecast_result[DATE_COL])
        + list(forecast_result[DATE_COL][::-1]),

        y=list(forecast_result["Upper Bound"])
        + list(forecast_result["Lower Bound"][::-1]),

        fill="toself",

        fillcolor="rgba(100, 149, 237, 0.15)",

        line=dict(
            color="rgba(255,255,255,0)"
        ),

        hoverinfo="skip",

        name="95% Confidence Interval"
    )
)


# Forecast start marker

fig.add_vline(
    x=last_date.timestamp() * 1000,
    line_dash="dot",
    annotation_text="Forecast Start"
)


fig.update_layout(
    height=500,
    hovermode="x unified",
    xaxis_title="Date",
    yaxis_title=metric,
    legend_title="Series"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# TREND INTERPRETATION
# ============================================================

st.markdown("## 🧠 Forecast Interpretation")


if change_pct > 5:

    st.warning(
        f"⚠️ The model indicates a potential increase of "
        f"{change_pct:.1f}% over the selected forecast horizon. "
        f"This may indicate increasing operational capacity pressure."
    )

elif change_pct < -5:

    st.success(
        f"🟢 The model indicates a potential decrease of "
        f"{abs(change_pct):.1f}% over the selected forecast horizon. "
        f"This may indicate easing system demand."
    )

else:

    st.info(
        f"🟡 The forecast indicates relative stability, "
        f"with an expected change of {change_pct:+.1f}%."
    )


# ============================================================
# FORECAST TABLE
# ============================================================

st.markdown("## 📋 Forecasted Values")

display_forecast = forecast_result.copy()

display_forecast[DATE_COL] = (
    display_forecast[DATE_COL]
    .dt.strftime("%Y-%m-%d")
)

display_forecast["Forecast"] = (
    display_forecast["Forecast"]
    .round(0)
    .astype(int)
)

display_forecast["Lower Bound"] = (
    display_forecast["Lower Bound"]
    .round(0)
    .astype(int)
)

display_forecast["Upper Bound"] = (
    display_forecast["Upper Bound"]
    .round(0)
    .astype(int)
)


st.dataframe(
    display_forecast,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# MODEL INFORMATION
# ============================================================

st.markdown("## ℹ️ Forecasting Method")

st.info(
    """
    **Forecasting approach:** Rolling-window linear trend.

    The model uses recent historical observations to estimate
    the underlying operational trend and projects that trend
    forward into the selected forecast horizon.

    The shaded area represents an approximate 95% confidence
    interval around the forecast.

    This transparent baseline is intended for operational
    planning and capacity monitoring.
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
