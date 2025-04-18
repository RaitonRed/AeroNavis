import pandas as pd
import numpy as np

FEATURE_COLUMNS = [
    'Latitude', 'Longitude', 'Altitude',
    'Speed', 'Direction',
    'Accel_X', 'Accel_Y', 'Accel_Z'
]

def load_processed_data(path="./data/processed_data"):
    try:
        # فایل CSV رو بخون
        df = pd.read_csv(path)

        # چک کنیم که آیا ستون‌ها موجود هستند یا خیر
        missing_columns = [col for col in FEATURE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

        # فقط ستون‌های مورد نظر رو جدا کن
        X = df[FEATURE_COLUMNS].values
        print(f"[✓] Data loaded successfully. Shape: {X.shape}")
        return X
    
    except FileNotFoundError:
        print(f"[✗] Error: The file at {path} was not found.")
        return None
    except ValueError as e:
        print(f"[✗] {e}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error: {e}")
        return None

    try:
        # فایل CSV رو بخون
        df = pd.read_csv(path)

        # چک کنیم که آیا ستون‌ها موجود هستند یا خیر
        missing_columns = [col for col in FEATURE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

        # فقط ستون‌های مورد نظر رو جدا کن
        X = df[FEATURE_COLUMNS].values
        print(f"[✓] Data loaded successfully. Shape: {X.shape}")
        return X
    
    except FileNotFoundError:
        print(f"[✗] Error: The file at {path} was not found.")
        return None
    except ValueError as e:
        print(f"[✗] {e}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error: {e}")
        return None

def load_data(path):
    try:
        # فایل CSV رو بخون
        df = pd.read_csv(path)

        # چک کنیم که آیا ستون‌ها موجود هستند یا خیر
        missing_columns = [col for col in FEATURE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

        # فقط ستون‌های مورد نظر رو جدا کن
        X = df[FEATURE_COLUMNS].values
        print(f"[✓] Data loaded successfully. Shape: {X.shape}")
        return X
    
    except FileNotFoundError:
        print(f"[✗] Error: The file at {path} was not found.")
        return None
    except ValueError as e:
        print(f"[✗] {e}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error: {e}")
        return None

    try:
        # فایل CSV رو بخون
        df = pd.read_csv(path)

        # چک کنیم که آیا ستون‌ها موجود هستند یا خیر
        missing_columns = [col for col in FEATURE_COLUMNS if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the dataset: {', '.join(missing_columns)}")

        # فقط ستون‌های مورد نظر رو جدا کن
        X = df[FEATURE_COLUMNS].values
        print(f"[✓] Data loaded successfully. Shape: {X.shape}")
        return X
    
    except FileNotFoundError:
        print(f"[✗] Error: The file at {path} was not found.")
        return None
    except ValueError as e:
        print(f"[✗] {e}")
        return None
    except Exception as e:
        print(f"[✗] Unexpected error: {e}")
        return None

if __name__ == '__main__':
    X = load_processed_data()
    if X is not None:
        print(f"[✓] Loaded data shape: {X.shape}")
