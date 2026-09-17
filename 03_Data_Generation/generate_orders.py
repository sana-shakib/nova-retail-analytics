import pandas as pd
import random
from faker import Faker
from datetime import date


fake = Faker()


customers = pd.read_csv("customers.csv")


orders = []


for i in range(30000):

    orders.append({

        "order_id": i + 1,

        "customer_id": random.choice(
            customers["customer_id"].tolist()
        ),

        "order_date": fake.date_between(
            start_date=date(2022,1,1),
            end_date=date(2025,12,31)
        ),

        "status": random.choice([
            "Completed",
            "Pending",
            "Cancelled"
        ]),

        "total_amount": random.randint(
            200000,
            20000000
        )

    })


df = pd.DataFrame(orders)


df.to_csv(
    "orders.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Orders dataset created ✅")
print(df.head())
print("Shape:", df.shape)