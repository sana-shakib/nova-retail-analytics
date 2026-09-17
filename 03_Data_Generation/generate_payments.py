import pandas as pd
import random
from datetime import date
from faker import Faker


fake = Faker()


sales = pd.read_csv("sales.csv")


payments = []


for i, row in sales.iterrows():

    payments.append({

        "payment_id": i + 1,

        "sale_id": int(row["sale_id"]),

        "payment_method": random.choice([
            "کارت بانکی",
            "درگاه آنلاین",
            "کیف پول",
            "نقدی"
        ]),

        "amount": int(row["total_amount"]),

        "payment_date": fake.date_between(
            start_date=date(2022,1,1),
            end_date=date(2025,12,31)
        )

    })


df = pd.DataFrame(payments)


df.to_csv(
    "payments.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Payments dataset created ✅")
print(df.head())
print("Shape:", df.shape)