import pandas as pd
import numpy as np

# مشخصات ویژگی‌ها
FEATURE_COLUMNS = [
    'Latitude', 'Longitude', 'Altitude',
    'Speed', 'Direction',
    'Accel_X', 'Accel_Y', 'Accel_Z'
]

def generate_dataset(num_samples=100):
    # داده‌های تصادفی برای ویژگی‌ها
    latitude = np.random.uniform(-90, 90, num_samples)  # Latitude
    longitude = np.random.uniform(-180, 180, num_samples)  # Longitude
    altitude = np.random.uniform(0, 5000, num_samples)  # Altitude
    speed = np.random.uniform(0, 150, num_samples)  # Speed
    direction = np.random.uniform(0, 360, num_samples)  # Direction
    accel_x = np.random.uniform(-10, 10, num_samples)  # Acceleration in X
    accel_y = np.random.uniform(-10, 10, num_samples)  # Acceleration in Y
    accel_z = np.random.uniform(-10, 10, num_samples)  # Acceleration in Z

    # ساخت دیتافریم
    df = pd.DataFrame({
        'Latitude': latitude,
        'Longitude': longitude,
        'Altitude': altitude,
        'Speed': speed,
        'Direction': direction,
        'Accel_X': accel_x,
        'Accel_Y': accel_y,
        'Accel_Z': accel_z
    })

    # محاسبه delta_yaw، delta_pitch و delta_thrust (تغییرات)
    df['delta_yaw'] = np.gradient(df['Direction'])
    df['delta_pitch'] = np.gradient(df['Altitude'])  # تغییرات در ارتفاع (نمونه)
    df['delta_thrust'] = np.gradient(df['Speed'])   # تغییرات در سرعت (نمونه)

    # ذخیره داده‌ها
    df.to_csv('./data/generated_data.csv', index=False)
    print(f"[✓] Generated {num_samples} samples and saved to './data/generated_data.csv'")

if __name__ == '__main__':
    generate_dataset()
