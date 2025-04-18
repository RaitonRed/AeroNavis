import pandas as pd

def load_data(input_path: str):
    """ بارگذاری داده‌ها از فایل CSV """
    return pd.read_csv(input_path)

def load_processed_data(input_path: str):
    """ بارگذاری داده‌های پیش‌پردازش شده """
    return pd.read_csv(input_path)
