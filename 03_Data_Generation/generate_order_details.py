import pandas as pd
import random


orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")


order_details = []


detail_id = 1


for order_id in orders["order_id"]:

    number_of_products = random.randint(1, 4)

    selected_products = products.sample(
        number_of_products
    )


    for _, product in selected_products.iterrows():

        quantity = random.randint(1, 5)


        order_details.append({

            "detail_id": detail_id,

            "order_id": order_id,

            "product_id": int(product["product_id"]),

            "quantity": quantity,

            "unit_price": int(product["price"])

        })


        detail_id += 1



df = pd.DataFrame(order_details)


df.to_csv(
    "order_details.csv",
    index=False,
    encoding="utf-8-sig"
)


print("Order Details dataset created ✅")
print(df.head())
print("Shape:", df.shape)