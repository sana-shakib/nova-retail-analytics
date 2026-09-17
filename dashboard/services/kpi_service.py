import streamlit as st
import pandas as pd

from services.data_source import get_sales_data


# =========================================================
# SALES KPIs
# =========================================================

@st.cache_data
def get_sales_kpis():

    df = get_sales_data()

    total_revenue = (
        df["total_amount"].sum()
    )

    total_transactions = (
        df["sale_id"].nunique()
    )

    total_quantity = (
        df["quantity"].sum()
    )

    average_sale = (
        total_revenue / total_transactions
        if total_transactions > 0
        else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_transactions": total_transactions,
        "total_quantity": total_quantity,
        "average_sale": average_sale
    }


# =========================================================
# CALCULATE SALES KPIs
# =========================================================

def calculate_sales_kpis(df):

    total_revenue = (
        df["total_amount"].sum()
    )

    total_transactions = (
        df["sale_id"].nunique()
    )

    total_quantity = (
        df["quantity"].sum()
    )

    average_order_value = (
        total_revenue / total_transactions
        if total_transactions > 0
        else 0
    )

    return {
        "total_revenue": total_revenue,
        "total_transactions": total_transactions,
        "total_quantity": total_quantity,
        "average_order_value": average_order_value
    }


# =========================================================
# MONTHLY REVENUE
# =========================================================

def monthly_revenue(df):

    data = df.copy()

    data["sale_date"] = pd.to_datetime(
        data["sale_date"]
    )

    result = (
        data
        .groupby(
            data["sale_date"].dt.to_period("M")
        )
        ["total_amount"]
        .sum()
        .reset_index()
    )

    result["sale_date"] = (
        result["sale_date"]
        .astype(str)
    )

    return result


# =========================================================
# BRANCH REVENUE
# =========================================================

def branch_revenue(df):

    return (
        df
        .groupby("branch_name")
        ["total_amount"]
        .sum()
        .reset_index()
        .sort_values(
            "total_amount",
            ascending=False
        )
    )


# =========================================================
# TOP PRODUCTS
# =========================================================

def top_products(df, limit=10):

    return (
        df
        .groupby("product_name")
        ["total_amount"]
        .sum()
        .reset_index()
        .sort_values(
            "total_amount",
            ascending=False
        )
        .head(limit)
    )