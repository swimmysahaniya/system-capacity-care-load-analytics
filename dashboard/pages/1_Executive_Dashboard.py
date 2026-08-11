import streamlit as st
import plotly.express as px
import pandas as pd

from utils import load_dataset
from components.layout import page_header, section
from components.cards import metric_card
from streamlit_extras.stylable_container import stylable_container

st.markdown("""
<style>

.kpi-card{
    background:linear-gradient(180deg,#111827,#0F172A);
    border-radius:14px;
    padding:18px;
    min-height:145px;
    transition:0.3s;
}

.kpi-card:hover{
    transform:translateY(-4px);
    transition:.25s;
    box-shadow:0 0 18px rgba(37,99,235,.25);
}

.border-blue{
    border:1.5px solid #2563EB;
}

.border-green{
    border:1.5px solid #16A34A;
}

.border-orange{
    border:1.5px solid #F59E0B;
}

.border-red{
    border:1.5px solid #DC2626;
}

.border-purple{
    border:1.5px solid #7C3AED;
}

.kpi-title{
    color:#9CA3AF;
    font-size:14px;
    font-weight:500;
}

.kpi-value{
    color:white;
    font-size:45px;
    font-weight:700;
    margin-top:10px;
    margin-bottom:12px;
}

.kpi-sub-delta{
    font-size:12px;
    padding-top: 5px;
    padding-left: 5px;
}

.kpi-delta-positive{
    display:inline-block;
    background:#0F5132;
    color:#22C55E;
    padding:6px 12px;
    border-radius:999px;
    font-size:14px;
    font-weight:600;
    margin-top:8px;
    margin-bottom:8px;
}

.kpi-delta-negative{
    display:inline-block;
    background:#5B1E24;
    color:#F87171;
    padding:6px 12px;
    border-radius:999px;
    font-size:14px;
    font-weight:600;
    margin-top:8px;
    margin-bottom:8px;
}

</style>
""", unsafe_allow_html=True)

df = load_dataset()

# ===========================
# Calculate KPI Values
# ===========================


current = int(df["Children in HHS Care"].iloc[-1])
previous = int(df["Children in HHS Care"].iloc[-2])
delta = current - previous

cbp = int(df["Children in CBP custody"].iloc[-1])
cbp_delta = cbp - int(df["Children in CBP custody"].iloc[-2])

transfer = int(df["Children transferred out of CBP custody"].iloc[-1])
transfer_delta = transfer - int(df["Children transferred out of CBP custody"].iloc[-2])

discharge = int(df["Children discharged from HHS Care"].iloc[-1])
discharge_delta = discharge - int(df["Children discharged from HHS Care"].iloc[-2])

occupancy = current / df["Children in HHS Care"].max() * 100

previous_occ = (
    df["Children in HHS Care"].iloc[-2]
    /
    df["Children in HHS Care"].max()
) * 100

occupancy_delta = occupancy - previous_occ

HIGH_OCCUPANCY = 90
MEDIUM_OCCUPANCY = 75

if occupancy > HIGH_OCCUPANCY:
    recommendation = "🔴 Critical Capacity"
    occ_color = "#EF4444"

elif occupancy > MEDIUM_OCCUPANCY:
    recommendation = "🟡 Prepare Additional Resources"
    occ_color = "#F59E0B"

else:
    recommendation = "🟢 Capacity Stable"
    occ_color = "#22C55E"

# ===========================
# Calculate KPI Values
# ===========================

page_header(
    "📊 Executive Dashboard",
    "High-level operational overview of the Unaccompanied Children program."
)

df["Date"] = pd.to_datetime(df["Date"])

latest_date = df["Date"].max().strftime("%d %b %Y")

st.markdown(
    f"""
    <div style="
    background:#111827;
    border:1px solid #334155;
    border-radius:12px;
    padding:16px 25px;
    margin-bottom:25px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    ">
    
    <div>
    🟢 <b>System</b> Operational
    </div>
    
    <div>
    📅 <b>Latest Data:</b> {latest_date}
    </div>
    
    <div>
    <span style="
    background:{occ_color};
    padding:6px 12px;
    border-radius:20px;
    font-weight:600;
    color:white;
    ">
    ⚡ <b>Recommendation:</b> {recommendation}
    </span>
    </div>
    
    <div>
    📊 <b>Capacity:</b> {occupancy:.1f}%
    </div>
    
    </div>
    """,
    unsafe_allow_html=True,
)

color_discrete_sequence = [
    "#2563EB",
    "#22C55E",
    "#F59E0B",
    "#EF4444"
]


def kpi_card(title, value, delta=None, percent=False, border="border-blue", value_color="#FFFFFF"):

    delta_html = ""

    if delta is not None:

        positive = delta >= 0

        badge = "kpi-delta-positive" if positive else "kpi-delta-negative"

        arrow = "▲" if positive else "▼"

        suffix = "%" if percent else ""

        delta_html = f""" 
        <div class="{badge}"> 
            {arrow} {abs(delta):,.1f}{suffix} 
        </div> """

        st.markdown(
            f""" 
            <div class="kpi-card {border}"> 
                <div class="kpi-title">{title}</div> 
                <div class="kpi-value" style="color:{value_color};">{value}</div> 
                {delta_html} 
                <div class="kpi-sub-delta">Compared to Previous Day</div> 
            </div> 
            """,
            unsafe_allow_html=True
        )


col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    kpi_card("🏥 Current HHS Care<br>Today's Count", f"{current:,}", delta, border="border-blue")

with col2:
    kpi_card("🚔 Current CBP<br>Today's Count", f"{cbp:,}", cbp_delta, border="border-orange")

with col3:
    kpi_card("🔄 Transfers<br>Today's Count", f"{transfer:,}", transfer_delta, border="border-purple")

with col4:
    kpi_card("✅ Discharges<br>Today's Count", f"{discharge:,}", discharge_delta, border="border-green")

with col5:
    kpi_card("📈 Occupancy<br>Today's Count", f"{occupancy:.1f}%", occupancy_delta, percent=True,
             border="border-red", value_color=occ_color)

# ===========================
# daily children in hhs care graph
# ===========================
current = int(df["Children in HHS Care"].iloc[-1])
peak = int(df["Children in HHS Care"].max())
average = int(df["Children in HHS Care"].mean())

with stylable_container(
    key="chart_card",
    css_styles="""
    {
        background: linear-gradient(180deg,#111827,#0F172A);
        border: 1px solid #334155;
        border-top:4px solid #2563EB;
        border-radius:18px;
        padding:20px;
        margin-top:30px;
    }
    """
):
    st.markdown("## 📈 Daily Children in HHS Care")
    st.caption("Jan 2023 – Dec 2025")

    fig = px.line(
        df,
        x="Date",
        y="Children in HHS Care"
    )

    fig.update_traces(
        line=dict(
            color="#60A5FA",
            width=3
        )
    )

    fig.update_layout(

        title="",

        paper_bgcolor="#111827",
        plot_bgcolor="#111827",

        font=dict(
            family="Inter",
            color="white",
            size=13
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        hovermode="x unified",

        xaxis=dict(
            showgrid=True,
            gridcolor="#334155",
            zeroline=False,
            title=""
        ),

        yaxis=dict(
            showgrid=True,
            gridcolor="#334155",
            zeroline=False,
            title="Children"
        ),

        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False
        }
    )
# ===========================
# daily children in hhs care graph end
# ===========================
with stylable_container(
    key="business_card",
    css_styles="""
    {
        background: linear-gradient(180deg,#111827,#0F172A);
        border: 1px solid #334155;
        border-top:4px solid #2563EB;
        border-radius:18px;
        padding:20px;
        margin-top:30px;
    }
    """
):

    # Heading
    st.markdown("## 📌 Business Interpretation")

    st.markdown("<div style='margin-bottom:30px;'></div>", unsafe_allow_html=True)

    # Description
    st.write("The HHS Care population experienced rapid growth during late 2023,followed by a sustained decline "
             "throughout 2024–2025.")

    st.write("The recent stabilization suggests improved operational efficiency, while continued monitoring is "
             "recommended to detect future capacity pressures.")

    st.divider()

    # Two charts
    left, right = st.columns(2)

    with left:
        st.markdown("### 📊 CBP Custody vs HHS Care")

        fig1 = px.line(
            df,
            x="Date",
            y=[
                "Children in CBP custody",
                "Children in HHS Care"
            ],
            title="📊 CBP Custody vs HHS Population"
        )

        fig1.update_traces(
            selector=dict(name="Children in CBP custody"),
            name="CBP"
        )

        fig1.update_traces(
            selector=dict(name="Children in HHS Care"),
            name="HHS Care"
        )

        fig1.update_layout(
            legend_title_text="",
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",

            height=420,

            margin=dict(
                l=10,
                r=10,
                t=20,  # Extra space for legend
                b=10
            ),

            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.08,  # Above chart
                xanchor="center",
                x=0.5,
                font=dict(size=12),
                bgcolor="rgba(0,0,0,0)"
            ),

            title=""
        )

        fig1.update_xaxes(showgrid=False)
        fig1.update_yaxes(gridcolor="#334155")

        st.plotly_chart(
            fig1,
            use_container_width=True,
            config={"displayModeBar": False}
        )

    with right:
        st.markdown("### 📉 Transfers vs Discharges")

        fig2 = px.line(
            df,
            x="Date",
            y=[
                "Children transferred out of CBP custody",
                "Children discharged from HHS Care"
            ],
            title="📉 Transfers vs Discharges",
            color_discrete_sequence=[
                "#F59E0B",  # Orange - Transfers
                "#22C55E"  # Green - Discharges
            ]
        )

        fig2.update_layout(
            legend_title_text="",
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font=dict(color="white"),

            height=420,

            margin=dict(
                l=10,
                r=10,
                t=20,  # Extra space for legend
                b=10
            ),

            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.08,  # Above chart
                xanchor="center",
                x=0.5,
                font=dict(size=12),
                bgcolor="rgba(0,0,0,0)"
            ),

            title=""
        )

        fig2.update_xaxes(showgrid=False)
        fig2.update_yaxes(gridcolor="#334155")

        st.plotly_chart(
            fig2,
            use_container_width=True,
            config={"displayModeBar": False}
        )

# ===========================
# executive summary and recommendation
# ===========================
CARD_STYLE = """
{
    background: linear-gradient(180deg,#111827,#0F172A);
    border:1px solid #334155;
    border-top:4px solid #2563EB;
    border-radius:18px;
    padding:25px;
    margin-top:25px;
}
"""

left, right = st.columns(2)

with left:

    with stylable_container(
        key="summary_card",
        css_styles=CARD_STYLE
    ):

        st.markdown("""
        <h4 style="
            color:white;
            margin-bottom:25px;
            font-size:25px;
            font-weight:700;">
            📄 Executive Summary
        </h4>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
            background:#111827;
            border-radius:16px;
            min-height:280px;
        ">
    
        <div style="display:flex;justify-content:space-between;padding:10px 0;">
            <span style="color:#94A3B8;">🟢 Current HHS Care</span>
            <b style="font-size:22px;color:white;">{current:,}</b>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="display:flex;justify-content:space-between;padding:10px 0;">
            <span style="color:#94A3B8;">🔵 Current CBP Custody</span>
            <b style="font-size:22px;color:white;">{cbp:,}</b>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="display:flex;justify-content:space-between;padding:10px 0;">
            <span style="color:#94A3B8;">🟠 Peak HHS Capacity</span>
            <b style="font-size:22px;color:#22C55E;">{df["Children in HHS Care"].max():,.0f}</b>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="display:flex;justify-content:space-between;padding:10px 0;">
            <span style="color:#94A3B8;">🟣 Avg Daily Transfers</span>
            <b style="font-size:22px;color:white;">{df["Children transferred out of CBP custody"].mean():.1f}</b>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="display:flex;justify-content:space-between;padding:10px 0;">
            <span style="color:#94A3B8;">🟢 Avg Daily Discharges</span>
            <b style="font-size:22px;color:white;">{df["Children discharged from HHS Care"].mean():.1f}</b>
        </div>
    
        </div>
        """, unsafe_allow_html=True)

with right:

    with stylable_container(
        key="recommendation_card",
        css_styles=CARD_STYLE
    ):

        st.markdown("""
        <h4 style="
            color:white;
            margin-bottom:25px;
            font-size:25px;
            font-weight:700;">
            💡 Operational Recommendations
        </h4>
        """, unsafe_allow_html=True)

        recommendations_html = f"""
        <div style="padding:7px 0;">
        <p style="margin: 6px 0;">
        <span style="color:#22C55E;font-size:18px;">✔</span>
        <span style="color:white;">
        Continue monitoring daily HHS occupancy.
        </span>
        </p>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="padding:7px 0;">
        <p style="margin: 6px 0;">
        <span style="color:#3B82F6;font-size:18px;">📈</span>
        <span style="color:white;">
        Watch for sudden increases in CBP custody.
        </span>
        </p>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="padding:7px 0;">
        <p style="margin: 6px 0;">
        <span style="color:#F59E0B;font-size:18px;">⚖️</span>
        <span style="color:white;">
        Compare transfers with discharge rates.
        </span>
        </p>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="padding:7px 0;">
        <p style="margin: 6px 0;">
        <span style="color:#A855F7;font-size:18px;">🔮</span>
        <span style="color:white;">
        Use forecasting results to anticipate future capacity needs.
        </span>
        </p>
        </div>
    
        <hr style="border:0.5px solid #334155; margin: revert;">
    
        <div style="padding:7px 0;">
        <p style="margin: 6px 0;">
        <span style="color:#EF4444;font-size:18px;">⚠️</span>
        <span style="color:white;">
        Monitor operational bottlenecks weekly.
        </span>
        </p>
        </div>
        """

        with st.container():
            st.markdown(
                recommendations_html,
                unsafe_allow_html=True
            )

# ===========================
# executive summary and recommendation end
# ===========================
# ===========================
# recent operational data
# ===========================
with stylable_container(
    key="recent_data_card",
    css_styles="""
    {
        background: linear-gradient(180deg,#111827,#0F172A);
        border:1px solid #334155;
        border-top:4px solid #2563EB;
        border-radius:18px;
        padding:20px;
        margin-top:30px;
    }
    """
):
    st.markdown("""
            <h2 style="
                color:white;
                font-size:34px;
                font-weight:700;">
                Recent Operational Data
            </h2>
            """, unsafe_allow_html=True)

    st.caption(
        f"Showing the latest 10 operational records from HHS dataset • Last Updated: {latest_date}"
    )

    recent = df.tail(10).iloc[::-1]

    table = recent.rename(columns={
        "Children apprehended and placed in CBP custody*": "Apprehended",
        "Children in CBP custody": "CBP",
        "Children transferred out of CBP custody": "Transfers",
        "Children in HHS Care": "HHS Care",
        "Children discharged from HHS Care": "Discharges"
    })

    table["Date"] = pd.to_datetime(table["Date"]).dt.strftime("%d %b %Y")

    st.dataframe(
        table.reset_index(drop=True),
        use_container_width=True
    )

    csv = table.to_csv(index=False)

    st.download_button(
        "📥 Download CSV",
        csv,
        file_name="recent_operational_data.csv",
        mime="text/csv"
    )

# ===========================
# recent operational data end
# ==========================
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
