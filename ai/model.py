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

model = build_gps_navigation_model()
model.summary()

# داده‌های تستی مجازی (فعلاً برای آموزش اولیه)
X_train = np.random.rand(5000, INPUT_SIZE)
y_train = np.random.rand(5000, OUTPUT_SIZE) * 2 - 1

model.fit(X_train, y_train, epochs=30, batch_size=32)

# ذخیره مدل
model.save("./models/base")
