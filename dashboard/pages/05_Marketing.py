import streamlit as st
import plotly.express as px

from services.marketing_service import (
    get_marketing_data,
    get_marketing_kpis
)


st.set_page_config(
    page_title="Marketing Analytics",
    layout="wide"
)


st.title("Marketing Analytics")
st.caption("Campaign Performance & ROI Analysis")


df = get_marketing_data()

kpis = get_marketing_kpis()



# KPI Section

c1, c2, c3 = st.columns(3)


c1.metric(
    "Total Campaigns",
    f"{kpis['total_campaigns']:,}"
)


c2.metric(
    "Total Budget",
    f"{kpis['total_budget']:,.0f}"
)


c3.metric(
    "Average ROI",
    f"{kpis['avg_roi']:.2f}"
)



st.divider()



# Campaign Table

st.subheader("Campaign Overview")


st.dataframe(
    df,
    use_container_width=True
)



# Budget Analysis

if "budget" in df.columns:

    budget = (
        df
        .sort_values(
            "budget",
            ascending=False
        )
        .head(10)
    )


    fig = px.bar(
        budget,
        x="campaign_name",
        y="budget",
        title="Top Campaigns by Budget"
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )



# Channel Analysis

if "channel" in df.columns:

    channel = (
        df.groupby("channel")
        .size()
        .reset_index(
            name="campaign_count"
        )
    )


    fig2 = px.pie(
        channel,
        names="channel",
        values="campaign_count",
        title="Campaign Distribution by Channel"
    )


    st.plotly_chart(
        fig2,
        use_container_width=True
    )