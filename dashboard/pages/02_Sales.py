import streamlit as st
import pandas as pd
import plotly.express as px

from services.sales_service import get_sales_analysis_data
from services.kpi_service import (
    calculate_sales_kpis,
    monthly_revenue,
    branch_revenue,
    top_products
)


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="تحلیل فروش | Sales Analytics",
    layout="wide"
)


# =========================
# Load Data
# =========================

@st.cache_data
def load_data():

    return get_sales_analysis_data()


df = load_data()


# =========================
# Title
# =========================

st.title(
    "تحلیل فروش | Sales Analytics"
)

st.caption(
    "Nova Retail Business Intelligence"
)


st.divider()


# =========================
# Filters
# =========================

col1, col2 = st.columns(2)


with col1:

    branches = [
        "همه شعب"
    ] + sorted(
        df["branch_name"]
        .unique()
        .tolist()
    )

    selected_branch = st.selectbox(
        "انتخاب شعبه | Branch",
        branches
    )


with col2:

    categories = [
        "همه دسته‌ها"
    ] + sorted(
        df["category"]
        .unique()
        .tolist()
    )

    selected_category = st.selectbox(
        "انتخاب دسته محصول | Category",
        categories
    )


filtered_df = df.copy()


if selected_branch != "همه شعب":

    filtered_df = filtered_df[
        filtered_df["branch_name"]
        == selected_branch
    ]


if selected_category != "همه دسته‌ها":

    filtered_df = filtered_df[
        filtered_df["category"]
        == selected_category
    ]


# =========================
# KPI
# =========================

kpis = calculate_sales_kpis(
    filtered_df
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "کل درآمد\nTotal Revenue",
        f"{kpis['total_revenue']:,.0f}"
    )


with col2:

    st.metric(
        "تعداد تراکنش\nTransactions",
        f"{kpis['total_transactions']:,}"
    )


with col3:

    st.metric(
        "تعداد کالا\nUnits Sold",
        f"{kpis['total_quantity']:,}"
    )


with col4:

    st.metric(
        "میانگین سفارش\nAverage Order",
        f"{kpis['average_order_value']:,.0f}"
    )


st.divider()


# =========================
# Monthly Revenue
# =========================

st.subheader(
    "روند درآمد ماهانه | Monthly Revenue Trend"
)


monthly = monthly_revenue(
    filtered_df
)


fig_month = px.line(
    monthly,
    x="sale_date",
    y="total_amount",
    markers=True
)


fig_month.update_layout(
    height=400,
    xaxis_title="ماه",
    yaxis_title="درآمد"
)


st.plotly_chart(
    fig_month,
    use_container_width=True
)


# =========================
# Branch Analysis
# =========================

col1, col2 = st.columns(2)


with col1:

    st.subheader(
        "عملکرد شعب | Branch Performance"
    )

    branch = branch_revenue(
        filtered_df
    )


    fig_branch = px.bar(
        branch,
        x="branch_name",
        y="total_amount"
    )


    st.plotly_chart(
        fig_branch,
        use_container_width=True
    )



with col2:

    st.subheader(
        "محصولات برتر | Top Products"
    )

    products = top_products(
        filtered_df
    )


    fig_products = px.bar(
        products,
        x="total_amount",
        y="product_name",
        orientation="h"
    )


    st.plotly_chart(
        fig_products,
        use_container_width=True
    )


# =========================
# Data Table
# =========================

st.divider()

st.subheader(
    "جزئیات فروش | Sales Details"
)


st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)