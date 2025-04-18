import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os
from data_loader import load_dataframe

RAW_PATH = './data/generated_data.csv'
PROCESSED_PATH = './data/processed_data.csv'

def preprocess_and_label(input_path=RAW_PATH, output_path=PROCESSED_PATH):
    """ داده‌های خام را پیش‌پردازش کرده و برچسب بزند """
    df = load_dataframe(input_path)

    # ساخت برچسب‌ها: مختصات گام بعدی
    df['Latitude_next'] = df['Latitude'].shift(-1)
    df['Longitude_next'] = df['Longitude'].shift(-1)
    df['Altitude_next'] = df['Altitude'].shift(-1)

    # حذف ردیف آخر چون Label نداره
    df.dropna(inplace=True)

    # لیست ستون‌های فیچر و لیبل
    feature_columns = [
        'Latitude', 'Longitude', 'Altitude',
        'Speed', 'Direction',
        'Accel_X', 'Accel_Y', 'Accel_Z'
    ]

    label_columns = [
        'Latitude_next', 'Longitude_next', 'Altitude_next'
    ]

    # نرمال‌سازی
    scaler = MinMaxScaler()
    features_scaled = pd.DataFrame(scaler.fit_transform(df[feature_columns]), columns=feature_columns)
    labels_scaled = pd.DataFrame(scaler.fit_transform(df[label_columns]), columns=label_columns)

    # ترکیب نهایی
    df_scaled = pd.concat([features_scaled, labels_scaled], axis=1)

    # ذخیره خروجی
    df_scaled.to_csv(output_path, index=False)
    print(f"[✓] Preprocessed & labeled data saved to {output_path}")

if __name__ == '__main__':
    preprocess_and_label()
