import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    'Latitude', 'Longitude', 'Altitude',
    'Speed', 'Direction',
    'Accel_X', 'Accel_Y', 'Accel_Z'
]

def load_processed_data(path='./data/processed_data.csv'):
    # فایل CSV رو بخون
    df = pd.read_csv(path)

    # فقط ستون‌های مورد نظر رو جدا کن
    X = df[FEATURE_COLUMNS].values

    return X

if __name__ == '__main__':
    X = load_processed_data()
    print(f"[✓] Loaded data shape: {X.shape}")
