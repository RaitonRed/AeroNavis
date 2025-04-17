import numpy as np
import pandas as pd
import random
import os

# مسیر ذخیره فایل CSV داده‌های تولیدی
DATA_PATH = './data/generated_gps_data.csv'

# تعداد نمونه‌هایی که باید تولید شوند
NUM_SAMPLES = 100

# تابع تولید داده‌های تصادفی
def generate_random_data(num_samples):
    data = []

    for _ in range(num_samples):
        # تولید داده‌های تصادفی برای GPS (طول جغرافیایی، عرض جغرافیایی، ارتفاع)
        latitude = random.uniform(-90.0, 90.0)  # عرض جغرافیایی
        longitude = random.uniform(-180.0, 180.0)  # طول جغرافیایی
        altitude = random.uniform(0, 10000)  # ارتفاع (متر)

        # تولید داده‌های دیگر مانند سرعت و جهت
        speed = random.uniform(0, 150)  # سرعت (کیلومتر در ساعت)
        direction = random.uniform(0, 360)  # جهت (درجه)

        # ذخیره داده‌ها در قالب یک لیست
        data.append([latitude, longitude, altitude, speed, direction])

    return data

# ذخیره داده‌ها در فایل CSV
def save_data_to_csv(data):
    # تبدیل داده‌ها به یک DataFrame
    df = pd.DataFrame(data, columns=['Latitude', 'Longitude', 'Altitude', 'Speed', 'Direction'])

    # ذخیره داده‌ها در فایل CSV
    df.to_csv(DATA_PATH, index=False)
    print(f"Data saved to {DATA_PATH}")

# تابع اصلی برای تولید و ذخیره داده‌ها
def main():
    # تولید داده‌ها
    data = generate_random_data(NUM_SAMPLES)

    # ذخیره داده‌ها در فایل CSV
    save_data_to_csv(data)

if __name__ == '__main__':
    main()
