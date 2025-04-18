import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

DATA_PATH = './data/generated_data.csv'
PROCESSED_PATH = './data/processed_data.csv'

def preprocess_data(input_path=DATA_PATH, output_path=PROCESSED_PATH):
    df = pd.read_csv(input_path)

    # ستون‌هایی که باید نرمال‌سازی بشن
    feature_columns = [
        'Latitude', 'Longitude', 'Altitude',
        'Speed', 'Direction',
        'Accel_X', 'Accel_Y', 'Accel_Z'
    ]

    scaler = MinMaxScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df[feature_columns]), columns=feature_columns)

    # ذخیره فایل نهایی
    df_scaled.to_csv(output_path, index=False)
    print(f"[✓] Preprocessed data saved to {output_path}")

if __name__ == '__main__':
    preprocess_data()
