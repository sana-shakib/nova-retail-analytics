import pandas as pd
from pathlib import Path


# مسیر فایل محصولات
BASE_DIR = Path(__file__).resolve().parent

products_path = BASE_DIR / "products.csv"


# خواندن محصولات
products = pd.read_csv(
    products_path
)


# لیست محصولات واقعی
product_names = [
    "کرم مرطوب کننده آبرسان",
    "سرم هیالورونیک اسید",
    "سرم ویتامین C",
    "کرم ضد آفتاب SPF50",
    "ژل شستشوی صورت",
    "کرم دور چشم",
    "ماسک صورت مغذی",
    "تونر پاک کننده پوست",
    "عطر ادو پرفیوم",
    "عطر زنانه کلاسیک",
    "عطر مردانه اسپرت",
    "اسپری بدن",
    "رژ لب مات",
    "ریمل حجم دهنده",
    "پنکیک آرایشی",
    "کرم پودر",
    "سایه چشم",
    "خط چشم ضد آب",
    "شامپو تقویت کننده",
    "نرم کننده مو",
    "کرم دست و بدن",
    "محصول مراقبت مو",
]


categories = [
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "مراقبت پوست",
    "عطر",
    "عطر",
    "عطر",
    "عطر",
    "آرایشی",
    "آرایشی",
    "آرایشی",
    "آرایشی",
    "آرایشی",
    "آرایشی",
    "بهداشتی",
    "بهداشتی",
    "بهداشتی",
    "بهداشتی",
]


brands = [
    "CeraVe",
    "The Ordinary",
    "La Roche-Posay",
    "Bioderma",
    "Neutrogena",
    "Eucerin",
    "Vichy",
    "L'Oréal",
    "Dior",
    "Chanel",
    "Armani",
    "Nivea",
    "Maybelline",
    "MAC",
    "NYX",
    "L'Oréal Paris",
    "Essence",
    "Sephora",
    "Head & Shoulders",
    "Pantene",
    "Nivea",
    "Garnier",
]


# جایگزینی داده‌ها
products["product_name"] = [
    product_names[i % len(product_names)]
    for i in range(len(products))
]


products["category"] = [
    categories[i % len(categories)]
    for i in range(len(products))
]


products["brand"] = [
    brands[i % len(brands)]
    for i in range(len(products))
]


# ذخیره
products.to_csv(
    products_path,
    index=False,
    encoding="utf-8-sig"
)


print("Product master data updated successfully")
print(products.head(10))
