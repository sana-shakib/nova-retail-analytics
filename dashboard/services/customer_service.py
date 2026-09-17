import pandas as pd

from services.sales_service import get_sales_analysis_data


def get_customer_analysis_data():

    """
    Customer Analytics Dataset

    RFM Analysis:
    - Recency
    - Frequency
    - Monetary

    Customer Segmentation:
    - VIP
    - Loyal
    - Potential
    - At Risk
    - Lost
    """

    sales = get_sales_analysis_data().copy()

    sales["sale_date"] = pd.to_datetime(
        sales["sale_date"]
    )

    # =====================================================
    # CUSTOMER AGGREGATION
    # =====================================================

    customer = (
        sales
        .groupby("customer_id")
        .agg(
            last_purchase=(
                "sale_date",
                "max"
            ),

            total_orders=(
                "sale_id",
                "count"
            ),

            total_revenue=(
                "total_amount",
                "sum"
            ),

            total_quantity=(
                "quantity",
                "sum"
            )
        )
        .reset_index()
    )

    # =====================================================
    # REFERENCE DATE
    # =====================================================

    reference_date = sales["sale_date"].max()

    # =====================================================
    # RFM FEATURES
    # =====================================================

    customer["recency"] = (
        reference_date
        - customer["last_purchase"]
    ).dt.days

    customer["frequency"] = (
        customer["total_orders"]
    )

    customer["monetary"] = (
        customer["total_revenue"]
    )

    # =====================================================
    # RFM SCORES
    # =====================================================

    customer["recency_score"] = pd.qcut(
        customer["recency"].rank(method="first"),
        5,
        labels=[5, 4, 3, 2, 1]
    ).astype(int)

    customer["frequency_score"] = pd.qcut(
        customer["frequency"].rank(method="first"),
        5,
        labels=[1, 2, 3, 4, 5]
    ).astype(int)

    customer["monetary_score"] = pd.qcut(
        customer["monetary"].rank(method="first"),
        5,
        labels=[1, 2, 3, 4, 5]
    ).astype(int)

    # =====================================================
    # RFM TOTAL SCORE
    # =====================================================

    customer["rfm_score"] = (
        customer["recency_score"]
        + customer["frequency_score"]
        + customer["monetary_score"]
    )

    # =====================================================
    # CUSTOMER SEGMENTATION
    # =====================================================

    def assign_segment(row):

        r = row["recency_score"]
        f = row["frequency_score"]
        m = row["monetary_score"]

        # VIP:
        # Recent + frequent + high value
        if r >= 4 and f >= 4 and m >= 4:
            return "VIP"

        # Loyal:
        # Frequent and valuable customers
        elif f >= 4 and m >= 3:
            return "Loyal"

        # Potential:
        # Recent customers with growth potential
        elif r >= 4 and f >= 2:
            return "Potential"

        # At Risk:
        # Previously valuable but not recently active
        elif r <= 2 and (f >= 3 or m >= 3):
            return "At Risk"

        # Lost:
        # Low recency + low engagement
        elif r <= 2 and f <= 2:
            return "Lost"

        # Remaining customers
        else:
            return "Potential"

    customer["segment"] = customer.apply(
        assign_segment,
        axis=1
    )

    return customer