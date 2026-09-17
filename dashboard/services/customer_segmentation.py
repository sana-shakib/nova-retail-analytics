import pandas as pd

from services.customer_service import get_customer_analysis_data



def get_customer_segments():

    """
    RFM Customer Segmentation Layer
    """


    customers = get_customer_analysis_data()


    data = customers.copy()



    # -----------------------------
    # RFM Score
    # -----------------------------

    data["recency_score"] = pd.qcut(
        data["recency"],
        5,
        labels=[5,4,3,2,1],
        duplicates="drop"
    )


    data["frequency_score"] = pd.qcut(
        data["frequency"]
        .rank(method="first"),
        5,
        labels=[1,2,3,4,5]
    )


    data["monetary_score"] = pd.qcut(
        data["monetary"],
        5,
        labels=[1,2,3,4,5]
    )


    data["rfm_score"] = (
        data["recency_score"].astype(int)
        +
        data["frequency_score"].astype(int)
        +
        data["monetary_score"].astype(int)
    )


    # -----------------------------
    # Customer Segments
    # -----------------------------

    def segment(row):

        if row["rfm_score"] >= 13:
            return "VIP"

        elif row["rfm_score"] >= 10:
            return "Loyal"

        elif row["recency_score"] >= 4:
            return "New Customer"

        else:
            return "At Risk"



    data["segment"] = data.apply(
        segment,
        axis=1
    )


    return data