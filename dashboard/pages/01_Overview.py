import streamlit as st
import plotly.express as px

from services.kpi_service import calculate_sales_kpis
from services.sales_service import get_sales_analysis_data
from services.customer_service import get_customer_analysis_data


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nova Retail Analytics",
    layout="wide"
)


# ============================================================
# HEADER
# ============================================================

st.title("Nova Retail Group - Business Overview")

st.caption(
    "Executive Dashboard | Sales, Customers & Business Performance"
)


# ============================================================
# LOAD DATA
# ============================================================

sales = get_sales_analysis_data()

customers = get_customer_analysis_data()

kpis = calculate_sales_kpis(sales)


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Revenue",
        f"{kpis['total_revenue']:,.0f}"
    )


with col2:
    st.metric(
        "Total Transactions",
        f"{kpis['total_transactions']:,}"
    )


with col3:
    st.metric(
        "Total Quantity Sold",
        f"{kpis['total_quantity']:,}"
    )


with col4:
    st.metric(
        "Average Sale",
        f"{kpis['average_order_value']:,.0f}"
    )


st.divider()


# ============================================================
# MONTHLY REVENUE TREND
# ============================================================

st.subheader("Monthly Revenue Trend")


monthly = (
    sales
    .groupby(
        sales["sale_date"].dt.to_period("M")
    )["total_amount"]
    .sum()
    .reset_index()
)


monthly["sale_date"] = (
    monthly["sale_date"]
    .astype(str)
)


fig = px.line(
    monthly,
    x="sale_date",
    y="total_amount",
    markers=True,
    title="Revenue Growth Over Time"
)


fig.update_layout(
    xaxis_title="Month",
    yaxis_title="Revenue"
)


st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# BRANCH PERFORMANCE
# ============================================================

st.subheader("Branch Performance")


branch = (
    sales
    .groupby("branch_name")["total_amount"]
    .sum()
    .reset_index()
    .sort_values(
        "total_amount",
        ascending=False
    )
)


fig2 = px.bar(
    branch,
    x="branch_name",
    y="total_amount",
    title="Revenue By Branch"
)


fig2.update_layout(
    xaxis_title="Branch",
    yaxis_title="Revenue"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)


# ============================================================
# TOP PRODUCTS
# ============================================================

st.subheader("Top Products")


products = (
    sales
    .groupby("product_name")["total_amount"]
    .sum()
    .reset_index()
    .sort_values(
        "total_amount",
        ascending=False
    )
    .head(10)
)


fig3 = px.bar(
    products,
    x="product_name",
    y="total_amount",
    title="Top 10 Products"
)


fig3.update_layout(
    xaxis_title="Product",
    yaxis_title="Revenue"
)


st.plotly_chart(
    fig3,
    use_container_width=True
)


# ============================================================
# CUSTOMER SUMMARY
# ============================================================

st.subheader("Customer Overview")


c1, c2, c3 = st.columns(3)


with c1:
    st.metric(
        "Customers",
        f"{len(customers):,}"
    )


with c2:
    st.metric(
        "VIP Customers",
        f"{(customers['segment'] == 'VIP').sum():,}"
    )


with c3:
    st.metric(
        "At Risk Customers",
        f"{(customers['segment'] == 'At Risk').sum():,}"
    )


# ============================================================
# CUSTOMER SEGMENT SUMMARY
# ============================================================

st.subheader("Customer Segmentation")


segment_summary = (
    customers["segment"]
    .value_counts()
    .reset_index()
)


segment_summary.columns = [
    "segment",
    "customers"
]


fig4 = px.bar(
    segment_summary,
    x="segment",
    y="customers",
    title="Customers by Segment"
)


fig4.update_layout(
    xaxis_title="Customer Segment",
    yaxis_title="Number of Customers"
)


st.plotly_chart(
    fig4,
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Nova Retail Business Intelligence Platform | Developed by Sana Shakib"
)