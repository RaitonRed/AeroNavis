import pandas as pd
import numpy as np

def load_processed_data(path='./data/processed_data.csv'):
    df = pd.read_csv(path)
    X = df.values[:, :-1]  # همه‌ی ستون‌ها به جز آخری (اگه لیبل نداری، همه‌ش X میشه)
    y = None  # اگه لیبل نداری، می‌تونی None بزاری یا بعداً اضافه‌ش کنی
    return X, y

if __name__ == '__main__':
    X, y = load_processed_data()
    print(f"Loaded data shape: {X.shape}")
