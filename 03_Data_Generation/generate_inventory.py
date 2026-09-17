import pandas as pd
import random
from datetime import date
from faker import Faker


fake = Faker()


products = pd.read_csv("products.csv")


inventory = []


for _, product in products.iterrows():

    inventory.append({

        "inventory_id": int(product["product_id"]),

        "product_id": int(product["product_id"]),

        "stock_quantity": random.randint(
            0,
            500
        ),

        "reorder_level": random.randint(
            20,
            100
        ),

        "update_date": fake.date_between(
            start_date=date(2025,1,1),
            end_date=date(2026,12,31)
        )

    })


df = pd.DataFrame(inventory)


df.to_csv(
    "inventory.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Inventory dataset created ✅")
print(df.head())
print("Shape:", df.shape)