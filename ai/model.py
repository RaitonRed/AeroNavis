import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Input
import numpy as np

# مشخصات ورودی/خروجی
INPUT_SIZE = 12  # GPS فعلی + GPS هدف + سرعت + جهت
OUTPUT_SIZE = 3  # delta_yaw, delta_pitch, delta_thrust

def build_gps_navigation_model():
    model = Sequential([
        Input(shape=(INPUT_SIZE,)),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(OUTPUT_SIZE, activation='tanh')  # خروجی بین -1 تا 1
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# ایجاد مدل
model = build_gps_navigation_model()

# نمایش ساختار مدل
model.summary()

# ذخیره مدل بدون آموزش
model.save("./models/model")  # مدل در مسیر مشخص شده ذخیره می‌شود
print("[✓] Model saved successfully.")
