import numpy as np
from keras.callbacks import ModelCheckpoint
from tensorflow.keras.callbacks import EarlyStopping
from keras.models import load_model
from utils.data_loader import load_processed_features_and_labels
from ai.model import build_navigation_model
import os
import sys

sys.path.append(os.path.abspath('.'))

# مسیر دیتاست
DATA_PATH = "./data/processed_data.csv"
# مسیر ذخیره مدل
MODEL_SAVE_PATH = "./models/model"

# 1. بارگذاری داده‌ها
X, y = load_processed_features_and_labels(DATA_PATH)
if X is None or y is None:
    print("[✗] Failed to load data. Exiting...")
    exit()

# 2. ساخت مدل
model = build_navigation_model()

# 3. آماده‌سازی برای ذخیره بهترین مدل حین آموزش
os.makedirs(os.path.dirname(MODEL_SAVE_PATH), exist_ok=True)
checkpoint = ModelCheckpoint(MODEL_SAVE_PATH, monitor='loss', save_best_only=True, verbose=1)

# 4. آموزش مدل
print("[🚀] Training started...")
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
model.fit(
    X_train, 
    y_train, 
    validation_data=(X_val, y_val), 
    epochs=50, 
    callbacks=[early_stop, checkpoint_cb]
)

print("[✓] Training complete.")
