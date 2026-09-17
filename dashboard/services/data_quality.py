import pandas as pd


def clean_product_data(df):

    """
    استانداردسازی اطلاعات محصولات
    Product Data Quality Layer
    """

    data = df.copy()


    # اصلاح نام ستون‌ها
    data.columns = (
        data.columns
        .str.strip()
    )


    # پاکسازی نام محصول
    if "product_name" in data.columns:

        data["product_name"] = (
            data["product_name"]
            .astype(str)
            .str.strip()
        )


    # دسته‌بندی محصول
    categories = [
        "مراقبت پوست",
        "عطر",
        "آرایشی",
        "بهداشتی"
    ]


    if "category" not in data.columns:

        data["category"] = [
            categories[i % len(categories)]
            for i in range(len(data))
        ]


    # برند استاندارد
    brands = [
        "Nova Beauty",
        "Luna Care",
        "Pure Skin",
        "Royal Essence",
        "Derma Plus"
    ]


    if "brand" not in data.columns:

        data["brand"] = [
            brands[i % len(brands)]
            for i in range(len(data))
        ]


    return data