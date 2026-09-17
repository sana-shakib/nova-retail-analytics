import pandas as pd

from config import DATA_DIR


def get_marketing_data():

    path = DATA_DIR / "marketing_campaigns.csv"

    df = pd.read_csv(path)

    return df



def get_marketing_kpis():

    df = get_marketing_data()


    result = {

        "total_campaigns": len(df),

        "total_budget": df["budget"].sum()
        if "budget" in df.columns
        else 0,

        "avg_roi": df["roi"].mean()
        if "roi" in df.columns
        else 0

    }


    return result