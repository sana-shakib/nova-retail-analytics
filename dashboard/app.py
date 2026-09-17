
import streamlit as st
from pathlib import Path
from textwrap import dedent
import pandas as pd

from config import (
    PAGE_TITLE,
    LAYOUT,
    PROJECT_NAME,
    PROJECT_VERSION,
    AUTHOR,
    REPORT_DIR,
)

from components.style_loader import load_css


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title=PAGE_TITLE,
    layout=LAYOUT,
    initial_sidebar_state="expanded",
)

load_css()


# =========================================================
# CONSTANTS
# =========================================================

DEFAULT_KPIS = {
    "revenue": 523_631_691_264,
    "transactions": 50_000,
    "average_sale": 10_472_634,
    "items": 150_147,
}


# =========================================================
# HTML RENDER HELPER
# =========================================================

def render_html(html):
    """
    Render raw HTML directly using Streamlit's HTML renderer.
    """

    st.html(dedent(html).strip())


# =========================================================
# KPI DATA
# =========================================================

@st.cache_data(ttl=3600)
def load_kpi_data():
    """
    Load KPI data from the sales KPI Excel report.

    If the report is unavailable, the dashboard
    falls back to the default project KPIs.
    """

    report_dir = Path(REPORT_DIR)

    possible_files = [
        report_dir / "شاخص_های_کلیدی_فروش.xlsx",
        report_dir / "شاخص‌های_کلیدی_فروش.xlsx",
        report_dir / "Ø´Ø§Ø®Øµ_Ù‡Ø§ÛŒ_Ú©Ù„ÛŒØ¯ÛŒ_ÙØ±ÙˆØ´.xlsx",
    ]

    for file_path in possible_files:

        if file_path.exists():

            try:
                return pd.read_excel(file_path)

            except Exception:
                return None

    return None


def extract_kpis(df):

    result = DEFAULT_KPIS.copy()

    if df is None or df.empty:
        return result

    kpi_column = None
    value_column = None

    possible_kpi_columns = [
        "شاخص",
        "KPI",
        "Metric",
        "metric",
        "Ø´Ø§Ø®Øµ",
    ]

    possible_value_columns = [
        "مقدار",
        "Value",
        "value",
        "Amount",
        "ØÙ‚Ø¯Ø§Ø±",
    ]

    for column in df.columns:

        if str(column).strip() in possible_kpi_columns:
            kpi_column = column
            break

    for column in df.columns:

        if str(column).strip() in possible_value_columns:
            value_column = column
            break

    if kpi_column is None or value_column is None:
        return result

    for _, row in df.iterrows():

        key = str(row[kpi_column]).strip()
        value = row[value_column]

        if pd.isna(value):
            continue

        try:
            numeric_value = float(value)

        except (ValueError, TypeError):
            continue

        if "درآمد" in key or "Revenue" in key:
            result["revenue"] = numeric_value

        elif "تراکنش" in key or "Transaction" in key:
            result["transactions"] = numeric_value

        elif "میانگین" in key or "Average" in key:
            result["average_sale"] = numeric_value

        elif "کالا" in key or "Unit" in key:
            result["items"] = numeric_value

    return result


sales_kpi = load_kpi_data()
kpis = extract_kpis(sales_kpi)


# =========================================================
# DESKTOP SIDEBAR
# =========================================================

with st.sidebar:

    render_html(
        """
        <div class="sidebar-brand">
            <div class="brand-name">NOVA</div>
            <div class="brand-subtitle">RETAIL GROUP</div>
        </div>
        """
    )

    render_html(
        """
        <div class="sidebar-section-title">
            NAVIGATION
        </div>
        """
    )

    # -----------------------------------------------------
    # Navigation
    # -----------------------------------------------------

    st.page_link(
        "app.py",
        label="نمای کلی",
        icon=None,
    )

    st.page_link(
        "pages/01_Overview.py",
        label="عملکرد کسب‌وکار",
        icon=None,
    )

    st.page_link(
        "pages/02_Sales.py",
        label="تحلیل فروش",
        icon=None,
    )

    st.page_link(
        "pages/04_Products.py",
        label="تحلیل محصولات",
        icon=None,
    )

    st.page_link(
        "pages/05_Marketing.py",
        label="تحلیل بازاریابی",
        icon=None,
    )

    st.page_link(
        "pages/06_Forecast.py",
        label="پیش‌بینی فروش",
        icon=None,
    )

    st.divider()

    # -----------------------------------------------------
    # Sidebar Meta
    # -----------------------------------------------------

    render_html(
        f"""
        <div class="sidebar-meta">
            <span>Platform</span>
            <strong>Business Intelligence</strong>

            <br><br>

            <span>Version</span>
            <strong>{PROJECT_VERSION}</strong>
        </div>
        """
    )


# =========================================================
# MOBILE NAVIGATION
# =========================================================

def render_mobile_navigation():

    with st.container(key="mobile_navigation"):

        with st.expander(
            "☰  Navigation",
            expanded=False,
        ):

            nav_col1, nav_col2 = st.columns(2)

            # -------------------------------------------------
            # COLUMN 1
            # -------------------------------------------------

            with nav_col1:

                st.page_link(
                    "app.py",
                    label="نمای کلی",
                    icon=None,
                )

                st.page_link(
                    "pages/01_Overview.py",
                    label="عملکرد کسب‌وکار",
                    icon=None,
                )

                st.page_link(
                    "pages/02_Sales.py",
                    label="تحلیل فروش",
                    icon=None,
                )

            # -------------------------------------------------
            # COLUMN 2
            # -------------------------------------------------

            with nav_col2:

                st.page_link(
                    "pages/04_Products.py",
                    label="تحلیل محصولات",
                    icon=None,
                )

                st.page_link(
                    "pages/05_Marketing.py",
                    label="تحلیل بازاریابی",
                    icon=None,
                )

                st.page_link(
                    "pages/06_Forecast.py",
                    label="پیش‌بینی فروش",
                    icon=None,
                )


# =========================================================
# RENDER MOBILE NAVIGATION
# =========================================================

render_mobile_navigation()


# =========================================================
# HEADER
# =========================================================

render_html(
    """
    <div class="page-header">

        <div>

            <div class="eyebrow">
                NOVA RETAIL GROUP
            </div>

            <h1>
                نمای کلی کسب‌وکار
            </h1>

            <div class="english-title">
                Business Intelligence Overview
            </div>

        </div>

        <div class="header-status">

            <span class="status-dot"></span>

            داده‌ها متصل هستند

        </div>

    </div>
    """
)


# =========================================================
# BUSINESS PROFILE
# =========================================================

render_html(
    """
    <div class="section-block">

        <div class="intro-label">
            BUSINESS PROFILE
        </div>

        <h2>
            Nova Retail Group
        </h2>

        <p>
            یک مجموعه خرده‌فروشی چندکاناله در حوزه
            محصولات آرایشی، عطر و مراقبت از پوست
            که عملکرد فروش، مشتریان، محصولات،
            بازاریابی و پیش‌بینی درآمد آن در این
            سامانه تحلیل می‌شود.
        </p>

        <div class="business-meta">

            <div>
                <span>مدل کسب‌وکار</span>
                <strong>B2C Retail</strong>
            </div>

            <div>
                <span>کانال فروش</span>
                <strong>Online &amp; Physical</strong>
            </div>

            <div>
                <span>دوره تحلیل</span>
                <strong>2022 — 2025</strong>
            </div>

            <div>
                <span>تعداد شعب</span>
                <strong>5 Branches</strong>
            </div>

        </div>

    </div>
    """
)


# =========================================================
# KPI SECTION
# =========================================================

render_html(
    """
    <div class="section-heading">

        <div>

            <h2>
                شاخص‌های کلیدی
            </h2>

            <span>
                Key Performance Indicators
            </span>

        </div>

    </div>
    """
)


# =========================================================
# KPI CARDS
# =========================================================

col1, col2, col3, col4 = st.columns(4)


# ---------------------------------------------------------
# Revenue
# ---------------------------------------------------------

with col1:

    render_html(
        f"""
        <div class="kpi-card">

            <div class="kpi-label">
                درآمد کل فروش
            </div>

            <div class="kpi-english">
                Total Revenue
            </div>

            <div class="kpi-value">
                {kpis["revenue"]:,.0f}
            </div>

            <div class="kpi-unit">
                IRR
            </div>

        </div>
        """
    )


# ---------------------------------------------------------
# Transactions
# ---------------------------------------------------------

with col2:

    render_html(
        f"""
        <div class="kpi-card">

            <div class="kpi-label">
                تعداد تراکنش
            </div>

            <div class="kpi-english">
                Transactions
            </div>

            <div class="kpi-value">
                {kpis["transactions"]:,.0f}
            </div>

            <div class="kpi-unit">
                Transactions
            </div>

        </div>
        """
    )


# ---------------------------------------------------------
# Average Sale
# ---------------------------------------------------------

with col3:

    render_html(
        f"""
        <div class="kpi-card">

            <div class="kpi-label">
                میانگین مبلغ فروش
            </div>

            <div class="kpi-english">
                Average Sale Value
            </div>

            <div class="kpi-value">
                {kpis["average_sale"]:,.0f}
            </div>

            <div class="kpi-unit">
                IRR / Transaction
            </div>

        </div>
        """
    )


# ---------------------------------------------------------
# Units Sold
# ---------------------------------------------------------

with col4:

    render_html(
        f"""
        <div class="kpi-card">

            <div class="kpi-label">
                تعداد کالاهای فروخته‌شده
            </div>

            <div class="kpi-english">
                Units Sold
            </div>

            <div class="kpi-value">
                {kpis["items"]:,.0f}
            </div>

            <div class="kpi-unit">
                Units
            </div>

        </div>
        """
    )


# =========================================================
# ANALYTICS AREAS
# =========================================================

render_html(
    """
    <div class="section-heading">

        <div>

            <h2>
                حوزه‌های تحلیلی
            </h2>

            <span>
                Analytics Areas
            </span>

        </div>

    </div>
    """
)


col1, col2, col3 = st.columns(3)


# ---------------------------------------------------------
# Sales Analytics
# ---------------------------------------------------------

with col1:

    render_html(
        """
        <div class="module-card">

            <div class="module-number">
                01
            </div>

            <h3>
                تحلیل فروش
            </h3>

            <span>
                Sales Analytics
            </span>

            <p>
                بررسی روند درآمد، تراکنش‌ها،
                عملکرد شعب و الگوهای زمانی فروش.
            </p>

        </div>
        """
    )


# ---------------------------------------------------------
# Customer Intelligence
# ---------------------------------------------------------

with col2:

    render_html(
        """
        <div class="module-card">

            <div class="module-number">
                02
            </div>

            <h3>
                تحلیل مشتریان
            </h3>

            <span>
                Customer Intelligence
            </span>

            <p>
                بررسی رفتار مشتریان، ارزش مشتری،
                خرید تکراری و بخش‌بندی مشتریان.
            </p>

        </div>
        """
    )


# ---------------------------------------------------------
# Machine Learning
# ---------------------------------------------------------

with col3:

    render_html(
        """
        <div class="module-card">

            <div class="module-number">
                03
            </div>

            <h3>
                پیش‌بینی درآمد
            </h3>

            <span>
                Machine Learning
            </span>

            <p>
                استفاده از مدل‌های یادگیری ماشین
                برای تحلیل و پیش‌بینی عملکرد فروش.
            </p>

        </div>
        """
    )


# =========================================================
# ANALYTICS PIPELINE
# =========================================================

render_html(
    """
    <div class="section-heading">

        <div>

            <h2>
                معماری تحلیل
            </h2>

            <span>
                Analytics Pipeline
            </span>

        </div>

    </div>
    """
)


render_html(
    """
    <div class="pipeline">

        <div>Data</div>

        <div>→</div>

        <div>SQL</div>

        <div>→</div>

        <div>EDA</div>

        <div>→</div>

        <div>Feature Engineering</div>

        <div>→</div>

        <div>Machine Learning</div>

        <div>→</div>

        <div>Business Intelligence</div>

    </div>
    """
)


# =========================================================
# FOOTER
# =========================================================

render_html(
    f"""
    <div class="footer">

        <span>
            {PROJECT_NAME}
        </span>

        <span>
            Data-driven Business Intelligence Platform
        </span>

        <span>
            {AUTHOR}
        </span>

    </div>
    """
)
