import pandas as pd
import random
from faker import Faker
from datetime import date


fake = Faker("fa_IR")


customers = pd.read_csv("customers.csv")


feedback = []


comments = [
    "کیفیت محصول عالی بود",
    "ارسال خیلی سریع انجام شد",
    "قیمت کمی بالا بود",
    "از خرید راضی هستم",
    "بسته بندی مناسب نبود",
    "محصول مشابه عکس بود",
    "کیفیت متوسط بود"
]


for i in range(8000):

    feedback.append({

        "feedback_id": i + 1,

        "customer_id": random.choice(
            customers["customer_id"].tolist()
        ),

        "rating": random.randint(1,5),

        "customer_comment": random.choice(
            comments
        ),

        "feedback_date": fake.date_between(
            start_date=date(2022,1,1),
            end_date=date(2026,12,31)
        )

    })


df = pd.DataFrame(feedback)


df.to_csv(
    "customer_feedback.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Customer Feedback dataset created ✅")
print(df.head())
print("Shape:", df.shape)