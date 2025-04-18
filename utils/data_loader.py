import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    'Latitude', 'Longitude', 'Altitude',
    'Speed', 'Direction',
    'Accel_X', 'Accel_Y', 'Accel_Z'
]

def load_dataframe(path="./data/generated_data.csv"):
    """ خواندن کل فایل به صورت DataFrame (برای پیش‌پردازش) """
    try:
        df = pd.read_csv(path)
        print(f"[✓] Full dataframe loaded. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        print(f"[✗] Error: File not found at {path}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error while loading dataframe: {e}")
        return None

def load_processed_features(path="./data/processed_data.csv"):
    """ فقط فیچرها (X) برای آموزش مدل """
    try:
        df = pd.read_csv(path)

        missing_columns = [col for col in FEATURE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

        X = df[FEATURE_COLUMNS].values
        print(f"[✓] Processed features loaded. Shape: {X.shape}")
        return X
    except FileNotFoundError:
        print(f"[✗] Error: File not found at {path}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error while loading features: {e}")
        return None

if __name__ == '__main__':
    # تست سریع
    load_dataframe()
    load_processed_features()
