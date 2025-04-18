import tensorflow as tf
from utils.data_loader import load_processed_data_with_labels
from model import build_navigation_model

# مسیر مدل ذخیره‌شده (در صورتی که مدل رو از قبل ذخیره کرده باشی)
MODEL_SAVE_PATH = "./models/trained_model"

# 1. بارگذاری داده‌ها
X, y = load_processed_data_with_labels()

# چک کن داده‌ها درست لود شده باشن
if X is None or y is None:
    raise Exception("[✗] Error: Failed to load training data")

# 2. ساخت مدل
model = build_navigation_model()

# 3. آموزش مدل
print("[→] Training model...")
model.fit(X, y, epochs=50, batch_size=32, validation_split=0.1)
print("[✓] Training complete!")

# 4. ذخیره مدل آموزش‌دیده
model.save(MODEL_SAVE_PATH)
print(f"[✓] Trained model saved at {MODEL_SAVE_PATH}")
