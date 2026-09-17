from faker import Faker
import pandas as pd
import random


fake = Faker("fa_IR")


products = []


categories = [
    "عطر",
    "محصولات پوستی",
    "آرایشی",
    "مراقبت مو",
    "بهداشتی"
]


brands = [
    "Dior",
    "Chanel",
    "L'Oréal",
    "Nivea",
    "Maybelline",
    "MAC",
    "The Ordinary"
]


for i in range(500):

    cost = random.randint(100000, 5000000)

    price = cost + random.randint(
        50000,
        2000000
    )

    products.append({

        "product_id": i + 1,

        "product_name": fake.word(),

        "category": random.choice(categories),

        "brand": random.choice(brands),

        "price": price,

        "cost": cost,

        "status": random.choice([
            "فعال",
            "غیرفعال"
        ])

    })


df = pd.DataFrame(products)


df.to_csv(
    "products.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Products dataset created ✅")
print(df.head())