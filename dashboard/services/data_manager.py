from pathlib import Path
import pandas as pd


class DataManager:

    def __init__(self, data_source="excel"):

        self.data_source = data_source


    # =====================================
    # Generic Reader
    # =====================================

    def _read_excel(self, file_path):

        return pd.read_excel(file_path)


    # =====================================
    # Sales
    # =====================================

    def load_sales_kpi(self, report_dir):

        file_path = (
            Path(report_dir)
            / "شاخص_های_کلیدی_فروش.xlsx"
        )

        return self._read_excel(file_path)


    def load_monthly_sales(self, report_dir):

        file_path = (
            Path(report_dir)
            / "روند_درآمد_ماهانه.xlsx"
        )

        return self._read_excel(file_path)


    # =====================================
    # Customers
    # =====================================

    def load_customers(self, report_dir):

        file_path = (
            Path(report_dir)
            / "تحلیل_مشتریان.xlsx"
        )

        return self._read_excel(file_path)


    # =====================================
    # Products
    # =====================================

    def load_products(self, report_dir):

        file_path = (
            Path(report_dir)
            / "تحلیل_محصولات.xlsx"
        )

        return self._read_excel(file_path)


    # =====================================
    # Marketing
    # =====================================

    def load_marketing(self, report_dir):

        file_path = (
            Path(report_dir)
            / "تحلیل_کمپین_ها.xlsx"
        )

        return self._read_excel(file_path)