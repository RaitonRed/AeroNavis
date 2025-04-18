import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    'Latitude', 'Longitude', 'Altitude',
    'Speed', 'Direction',
    'Accel_X', 'Accel_Y', 'Accel_Z'
]

LABEL_COLUMNS = [
    'Latitude_next', 'Longitude_next', 'Altitude_next'
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


def load_processed_features_and_labels(path="./data/processed_data.csv"):
    """ لود فیچرها و لیبل‌ها برای آموزش مدل """
    try:
        df = pd.read_csv(path)

        # چک کنیم که ستون‌ها وجود دارند
        missing_features = [col for col in FEATURE_COLUMNS if col not in df.columns]
        missing_labels = [col for col in LABEL_COLUMNS if col not in df.columns]
        if missing_features or missing_labels:
            raise ValueError(
                f"Missing columns in the dataset: {', '.join(missing_features + missing_labels)}"
            )

        X = df[FEATURE_COLUMNS].values
        y = df[LABEL_COLUMNS].values
        print(f"[✓] Features and labels loaded. X shape: {X.shape}, y shape: {y.shape}")
        return X, y
    except FileNotFoundError:
        print(f"[✗] Error: File not found at {path}")
        return None, None
    except Exception as e:
        print(f"[✗] Unexpected error while loading features and labels: {e}")
        return None, None


if __name__ == '__main__':
    # تست سریع
    df = load_dataframe()
    X, y = load_processed_features_and_labels()
