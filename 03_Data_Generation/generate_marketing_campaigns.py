import pandas as pd
import random
from faker import Faker
from datetime import date


fake = Faker()


campaigns = []


channels = [
    "Instagram",
    "Google Ads",
    "Email Marketing",
    "SMS",
    "Website"
]


for i in range(50):

    campaigns.append({

        "campaign_id": i + 1,

        "campaign_name": f"Campaign_{i+1}",

        "channel": random.choice(channels),

        "budget": random.randint(
            5000000,
            200000000
        ),

        "start_date": fake.date_between(
            start_date=date(2022,1,1),
            end_date=date(2025,12,31)
        ),

        "end_date": fake.date_between(
            start_date=date(2023,1,1),
            end_date=date(2026,12,31)
        )

    })


df = pd.DataFrame(campaigns)


df.to_csv(
    "marketing_campaigns.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Marketing Campaigns dataset created ✅")
print(df.head())
print("Shape:", df.shape)