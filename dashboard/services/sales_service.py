import streamlit as st
import pandas as pd

from config import DATA_DIR
from services.data_source import get_sales_data
from services.data_quality import clean_product_data
@st.cache_data
def load_products():

    path = DATA_DIR / "products.csv"

    products = pd.read_csv(path)

    return products


@st.cache_data
def load_branches():

    path = DATA_DIR / "branches.csv"

    branches = pd.read_csv(path)

    return branches

def get_sales_analysis_data():

    sales = get_sales_data()

    products = load_products()

    branches = load_branches()


    if "product_id" in products.columns:

        sales = sales.merge(
            products,
            on="product_id",
            how="left"
        )


    if "branch_id" in branches.columns:

        sales = sales.merge(
            branches,
            on="branch_id",
            how="left"
        )
    sales = clean_product_data(sales)

    return sales