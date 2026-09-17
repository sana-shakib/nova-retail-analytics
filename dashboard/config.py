from pathlib import Path



# =========================================================
# Project Information
# =========================================================

PROJECT_NAME = "سامانه هوشمند تحلیل کسب‌وکار Nova Retail"

PROJECT_VERSION = "نسخه ۱.۰"

AUTHOR = "Sana Shakib"


# =========================================================
# Streamlit Settings
# =========================================================

PAGE_TITLE = "تحلیل کسب‌وکار Nova Retail"

PAGE_ICON = None

LAYOUT = "wide"


# =========================================================
# Project Paths
# =========================================================

# Root project directory:
# C:\Users\S\OneDrive\Desktop\ملکیان\nova

BASE_DIR = Path(__file__).resolve().parent.parent


# Dashboard

DASHBOARD_DIR = (
    BASE_DIR / "dashboard"
)


# Raw / generated data

DATA_DIR = (
    BASE_DIR / "03_Data_Generation"
)


# Python analysis

PYTHON_ANALYSIS_DIR = (
    BASE_DIR / "07_Python_Analysis"
)


# Analysis outputs

OUTPUT_DIR = (
    PYTHON_ANALYSIS_DIR / "outputs"
)


# Final management reports

REPORT_DIR = (
    OUTPUT_DIR / "گزارش_نهایی_مدیریتی"
)


# Dashboard assets

ASSETS_DIR = (
    DASHBOARD_DIR / "assets"
)


# =========================================================
# Theme
# =========================================================

PRIMARY_COLOR = "#0F172A"

SECONDARY_COLOR = "#2563EB"

SUCCESS_COLOR = "#16A34A"

WARNING_COLOR = "#F59E0B"

DANGER_COLOR = "#DC2626"

BACKGROUND_COLOR = "#F8FAFC"

CARD_COLOR = "#FFFFFF"
