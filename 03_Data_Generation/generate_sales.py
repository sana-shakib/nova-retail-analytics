import pandas as pd
import random
from faker import Faker
from datetime import date


fake = Faker()


customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
branches = pd.read_csv("branches.csv")


sales = []


for i in range(50000):

    product = products.sample(1).iloc[0]

    quantity = random.randint(1, 5)

    total_amount = int(product["price"]) * quantity


    sales.append({
        "sale_id": i + 1,

        "customer_id": random.choice(
            customers["customer_id"].tolist()
        ),

        "product_id": int(product["product_id"]),

        "branch_id": random.choice(
            branches["branch_id"].tolist()
        ),

        "sale_date": fake.date_between(
            start_date=date(2022, 1, 1),
            end_date=date(2025, 12, 31)
        ),

        "quantity": quantity,

        "total_amount": total_amount
    })


df = pd.DataFrame(sales)


df.to_csv(
    "sales.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Sales dataset created ✅")
print(df.head())
print("Shape:", df.shape)