import pandas as pd
import streamlit as st

from config import DATA_DIR


@st.cache_data
def get_sales_history():

    path = DATA_DIR / "sales.csv"

    if not path.exists():
        raise FileNotFoundError(
            f"Sales data not found: {path}"
        )

    df = pd.read_csv(path)

    df["sale_date"] = pd.to_datetime(
        df["sale_date"],
        errors="coerce"
    )

    df["total_amount"] = pd.to_numeric(
        df["total_amount"],
        errors="coerce"
    )

    df = df.dropna(
        subset=[
            "sale_date",
            "total_amount"
        ]
    )

    return df


@st.cache_data
def prepare_monthly_sales():

    df = get_sales_history()

    monthly = (
        df
        .assign(
            sale_month=df["sale_date"].dt.to_period("M")
        )
        .groupby("sale_month", as_index=False)["total_amount"]
        .sum()
    )

    monthly["sale_date"] = (
        monthly["sale_month"]
        .dt.to_timestamp()
    )

    monthly = monthly.rename(
        columns={
            "total_amount": "revenue"
        }
    )

    monthly = (
        monthly[
            [
                "sale_date",
                "revenue"
            ]
        ]
        .sort_values("sale_date")
        .reset_index(drop=True)
    )

    return monthly