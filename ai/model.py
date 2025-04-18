import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Input
from tensorflow.keras.layers import Dropout
import numpy as np

# مشخصات ورودی/خروجی
INPUT_SIZE = 8  # GPS فعلی + GPS هدف + سرعت + جهت
OUTPUT_SIZE = 3  # delta_yaw, delta_pitch, delta_thrust

def build_navigation_model():
    model = Sequential([
        Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        Dropout(0.3),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(3, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# ایجاد مدل
model = build_navigation_model()

# نمایش ساختار مدل
model.summary()

# ذخیره مدل بدون آموزش
model.save("./models/model")  # مدل در مسیر مشخص شده ذخیره می‌شود
print("[✓] Model saved successfully.")
