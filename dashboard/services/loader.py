import pandas as pd


def load_excel(file_path):

    """
    خواندن فایل Excel
    """

    df = pd.read_excel(
        file_path
    )

    return df