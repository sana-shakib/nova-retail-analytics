import streamlit as st
from pathlib import Path
import pandas as pd

from config import DATA_DIR


def _sales_file():
    return Path(DATA_DIR) / "sales.csv"


@st.cache_data
def load_sales_data():

    file_path = _sales_file()

    if not file_path.exists():
        raise FileNotFoundError(
            f"Sales data not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    if "sale_date" in df.columns:
        df["sale_date"] = pd.to_datetime(
            df["sale_date"],
            errors="coerce"
        )

    if "total_amount" in df.columns:
        df["total_amount"] = pd.to_numeric(
            df["total_amount"],
            errors="coerce"
        )

    if "quantity" in df.columns:
        df["quantity"] = pd.to_numeric(
            df["quantity"],
            errors="coerce"
        )

    df = df.dropna(
        subset=["sale_date", "total_amount"]
    )

    return df


def get_sales_data():
    """
    Public API for sales data.
    Returns cached and cleaned sales data.
    """

    return load_sales_data()