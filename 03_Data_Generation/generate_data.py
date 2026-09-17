from faker import Faker
import pandas as pd
import random
from datetime import datetime


fake = Faker("fa_IR")


customers = []

for i in range(10000):

    customers.append({

        "customer_id": i + 1,
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birth_date": fake.date_of_birth(
            minimum_age=18,
            maximum_age=70
        ),
        "city": random.choice([
            "شیراز",
            "تهران",
            "اصفهان",
            "مشهد",
            "تبریز"
        ]),
        "created_date": fake.date_between(
            start_date="-3y",
            end_date="today"
        )

    })


df = pd.DataFrame(customers)


df.to_csv(
    "customers.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Customers dataset created ✅")
print(df.head())
