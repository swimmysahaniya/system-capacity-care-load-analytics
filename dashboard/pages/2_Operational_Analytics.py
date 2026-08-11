import streamlit as st
import pandas as pd
import plotly.express as px

from utils import load_dataset
from components.layout import page_header, section


# ============================================================
# PAGE SETUP
# ============================================================

page_header(
    "📈 Operational Analytics",
    "Detailed analysis of system activity, transfers, discharges, and care capacity."
)


# ============================================================
# LOAD DATA
# ============================================================

df = load_dataset()


# ============================================================
# NORMALIZE COLUMN NAMES
# ============================================================

df.columns = df.columns.str.strip()


# ============================================================
# COLUMN DEFINITIONS
# ============================================================

DATE_COL = "Date"
APPREHENDED_COL = "Children apprehended and placed in CBP custody*"
CBP_COL = "Children in CBP custody"
TRANSFERS_COL = "Children transferred out of CBP custody"
HHS_COL = "Children in HHS Care"
DISCHARGES_COL = "Children discharged from HHS Care"


# ============================================================
# VALIDATE DATASET
# ============================================================

required_columns = [
    DATE_COL,
    APPREHENDED_COL,
    CBP_COL,
    TRANSFERS_COL,
    HHS_COL,
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

min_date = df[DATE_COL].min().date()
max_date = df[DATE_COL].max().date()


# ============================================================
# ANALYSIS PERIOD
# ============================================================

st.markdown("## 📅 Analysis Period")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input(
        "Start Date",
        value=min_date,
        min_value=min_date,
        max_value=max_date
    )

with col2:
    end_date = st.date_input(
        "End Date",
        value=max_date,
        min_value=min_date,
        max_value=max_date
    )


# ============================================================
# VALIDATE DATE RANGE
# ============================================================

if start_date > end_date:

    st.error("Start Date cannot be after End Date.")

    st.stop()


# ============================================================
# FILTER DATA
# ============================================================

filtered_df = df[
    (df[DATE_COL].dt.date >= start_date)
    &
    (df[DATE_COL].dt.date <= end_date)
].copy()


if filtered_df.empty:

    st.warning(
        "No data available for the selected date range."
    )

    st.stop()


# ============================================================
# KPI CALCULATIONS
# ============================================================

avg_hhs = filtered_df[HHS_COL].mean()

avg_cbp = filtered_df[CBP_COL].mean()

avg_transfers = filtered_df[TRANSFERS_COL].mean()

avg_discharges = filtered_df[DISCHARGES_COL].mean()

peak_hhs = filtered_df[HHS_COL].max()

peak_cbp = filtered_df[CBP_COL].max()

total_transfers = filtered_df[TRANSFERS_COL].sum()

total_discharges = filtered_df[DISCHARGES_COL].sum()


# ============================================================
# KPI DISPLAY
# ============================================================

st.markdown("## 📊 Key Operational Metrics")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Average HHS Care",
        f"{avg_hhs:,.0f}"
    )

with c2:
    st.metric(
        "Average CBP Custody",
        f"{avg_cbp:,.0f}"
    )

with c3:
    st.metric(
        "Average Transfers",
        f"{avg_transfers:,.1f}"
    )

with c4:
    st.metric(
        "Average Discharges",
        f"{avg_discharges:,.1f}"
    )


# ============================================================
# HHS CARE TREND
# ============================================================

st.markdown("## 👶 HHS Care Population")

fig_hhs = px.line(
    filtered_df,
    x=DATE_COL,
    y=HHS_COL,
    title="Children in HHS Care Over Time",
    labels={
        DATE_COL: "Date",
        HHS_COL: "Children in HHS Care"
    }
)

fig_hhs.update_layout(
    height=450,
    hovermode="x unified"
)

st.plotly_chart(
    fig_hhs,
    use_container_width=True
)


# ============================================================
# CBP VS HHS
# ============================================================

st.markdown("## 🏛️ CBP Custody vs HHS Care")

fig_care = px.line(
    filtered_df,
    x=DATE_COL,
    y=[CBP_COL, HHS_COL],
    title="CBP Custody vs HHS Care",
    labels={
        "value": "Children",
        "variable": "Metric",
        DATE_COL: "Date"
    }
)

fig_care.update_layout(
    height=450,
    hovermode="x unified"
)

st.plotly_chart(
    fig_care,
    use_container_width=True
)


# ============================================================
# TRANSFERS VS DISCHARGES
# ============================================================

st.markdown("## 🔄 Transfers vs Discharges")

fig_flow = px.line(
    filtered_df,
    x=DATE_COL,
    y=[TRANSFERS_COL, DISCHARGES_COL],
    title="Transfers and Discharges Over Time",
    labels={
        "value": "Children",
        "variable": "Metric",
        DATE_COL: "Date"
    }
)

fig_flow.update_layout(
    height=450,
    hovermode="x unified"
)

st.plotly_chart(
    fig_flow,
    use_container_width=True
)


# ============================================================
# OPERATIONAL SUMMARY
# ============================================================

st.markdown("## 📌 Operational Summary")

s1, s2, s3 = st.columns(3)

with s1:
    st.metric(
        "Peak HHS Care",
        f"{peak_hhs:,.0f}"
    )

with s2:
    st.metric(
        "Peak CBP Custody",
        f"{peak_cbp:,.0f}"
    )

with s3:
    st.metric(
        "Total Transfers",
        f"{total_transfers:,.0f}"
    )


# ============================================================
# DATA PREVIEW
# ============================================================

st.markdown("## 📋 Filtered Operational Data")

st.dataframe(
    filtered_df[
        [
            DATE_COL,
            APPREHENDED_COL,
            CBP_COL,
            TRANSFERS_COL,
            HHS_COL,
            DISCHARGES_COL
        ]
    ],
    use_container_width=True,
    hide_index=True
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
