import pandas as pd


def load_excel(file_path):
    """
    Load Excel file safely.
    """
    try:
        return pd.read_excel(file_path)

    except Exception as e:
        raise Exception(f"Error loading Excel file:\n{e}")


def load_csv(file_path):
    """
    Load CSV file safely.
    """
    try:
        return pd.read_csv(file_path)

    except Exception as e:
        raise Exception(f"Error loading CSV file:\n{e}")