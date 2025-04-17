import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
import numpy as np

# تعریف پارامترها
INPUT_SIZE = 9   # x, y, z, vx, vy, vz, yaw, pitch, roll
OUTPUT_SIZE = 3  # delta_yaw, delta_pitch, delta_roll

# ساخت مدل
def build_model():
    model = Sequential([
        Input(shape=(INPUT_SIZE,)),
        Dense(64, activation='relu'),
        Dense(64, activation='relu'),
        Dense(OUTPUT_SIZE, activation='tanh')  # خروجی بین -1 تا 1
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

# مدل رو بسازیم
model = build_model()
model.summary()

# داده‌های مجازی برای آموزش تستی
X_train = np.random.rand(1000, INPUT_SIZE)
y_train = np.random.rand(1000, OUTPUT_SIZE) * 2 - 1  # خروجی بین -1 تا 1

# آموزش مدل
model.fit(X_train, y_train, epochs=20, batch_size=32)

# ذخیره مدل
model.save("ai/saved_model/aeronavis_model")
