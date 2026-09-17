import pandas as pd


def check_data_quality(df):

    """
    بررسی کیفیت داده
    """

    report = {

        "تعداد رکورد": len(df),

        "تعداد ستون": len(df.columns),

        "مقادیر خالی": int(
            df.isnull().sum().sum()
        ),

        "رکوردهای تکراری": int(
            df.duplicated().sum()
        )

    }


    return report



def validate_required_columns(
        df,
        required_columns
):

    """
    بررسی وجود ستون‌های ضروری
    """

    missing = []

    for col in required_columns:

        if col not in df.columns:

            missing.append(col)


    return missing