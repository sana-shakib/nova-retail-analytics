import pandas as pd
from datetime import date


branches = [

    {
        "branch_id": 1,
        "branch_name": "شعبه مرکزی",
        "city": "شیراز",
        "opening_date": "2022-01-15"
    },

    {
        "branch_id": 2,
        "branch_name": "شعبه شمال",
        "city": "تهران",
        "opening_date": "2022-05-20"
    },

    {
        "branch_id": 3,
        "branch_name": "شعبه شرق",
        "city": "مشهد",
        "opening_date": "2023-02-10"
    },

    {
        "branch_id": 4,
        "branch_name": "شعبه اصفهان",
        "city": "اصفهان",
        "opening_date": "2023-08-01"
    },

    {
        "branch_id": 5,
        "branch_name": "شعبه تبریز",
        "city": "تبریز",
        "opening_date": "2024-03-12"
    }

]


df = pd.DataFrame(branches)


df.to_csv(
    "branches.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Branches dataset created ✅")
print(df)