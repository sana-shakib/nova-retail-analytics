import streamlit as st
import pandas as pd

from services.sales_service import get_sales_analysis_data


# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Product Analytics | Nova Retail",
    page_icon="📦",
    layout="wide"
)


# =====================================================
# Load Data
# =====================================================

@st.cache_data
def load_data():

    df = get_sales_analysis_data()

    return df


sales = load_data()


# =====================================================
# Header
# =====================================================

st.title("📦 Product Analytics")

st.caption(
    "تحلیل عملکرد محصولات | Product Performance Analysis"
)


st.divider()


# =====================================================
# Feature Engineering
# =====================================================

sales["profit"] = (
    sales["total_amount"]
    -
    (sales["cost"] * sales["quantity"])
)


# =====================================================
# KPI Section
# =====================================================

total_products = (
    sales["product_name"]
    .nunique()
)


total_revenue = (
    sales["total_amount"]
    .sum()
)


total_profit = (
    sales["profit"]
    .sum()
)


best_category = (
    sales.groupby("category")
    ["total_amount"]
    .sum()
    .idxmax()
)



col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "Total Products",
        f"{total_products:,}"
    )


with col2:

    st.metric(
        "Revenue",
        f"{total_revenue/1e9:.1f} B"
    )


with col3:

    st.metric(
        "Gross Profit",
        f"{total_profit/1e9:.1f} B"
    )


with col4:

    st.metric(
        "Best Category",
        best_category
    )


st.divider()


# =====================================================
# Category Revenue
# =====================================================

st.subheader(
    "Revenue by Category"
)


category_sales = (
    sales
    .groupby("category")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
)


st.bar_chart(
    category_sales
)



st.divider()


# =====================================================
# Top Products
# =====================================================


st.subheader(
    "Top 10 Products"
)


top_products = (

    sales
    .groupby(
        [
            "product_name",
            "brand"
        ]
    )
    .agg(
        revenue=(
            "total_amount",
            "sum"
        ),

        profit=(
            "profit",
            "sum"
        )
    )
    .sort_values(
        "revenue",
        ascending=False
    )
    .head(10)
    .reset_index()

)


st.dataframe(
    top_products,
    use_container_width=True
)



st.divider()


# =====================================================
# Brand Performance
# =====================================================


st.subheader(
    "Brand Performance"
)


brand_analysis = (

    sales
    .groupby("brand")
    ["total_amount"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)

)


st.bar_chart(
    brand_analysis
)



st.divider()


# =====================================================
# Profitability Table
# =====================================================


st.subheader(
    "Product Profitability"
)


profit_table = (

    sales
    .groupby(
        "product_name"
    )
    .agg(

        Revenue=(
            "total_amount",
            "sum"
        ),

        Profit=(
            "profit",
            "sum"
        )

    )

    .sort_values(
        "Profit",
        ascending=False
    )

    .head(15)

)


st.dataframe(
    profit_table,
    use_container_width=True
)



# =====================================================
# Footer
# =====================================================

st.caption(
    "Nova Retail Business Intelligence Platform | Developed by Sana Shakib"
)