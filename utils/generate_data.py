import numpy as np
import pandas as pd
import random
import os

DATA_PATH = './data/generated_data.csv'
NUM_SAMPLES = 200

def generate_random_data(num_samples):
    data = []

    for _ in range(num_samples):
        # GPS data
        latitude = random.uniform(-90.0, 90.0)
        longitude = random.uniform(-180.0, 180.0)
        altitude = random.uniform(0, 500)  # متر

        # Movement info
        speed = random.uniform(0, 100)  # km/h
        direction = random.uniform(0, 360)  # degrees

        # Accelerometer data (m/s²)
        accel_x = random.uniform(-5.0, 5.0)
        accel_y = random.uniform(-5.0, 5.0)
        accel_z = random.uniform(-10.0, 10.0)  # چون g=9.8

        data.append([
            latitude, longitude, altitude,
            speed, direction,
            accel_x, accel_y, accel_z
        ])

    return data

def save_data_to_csv(data):
    columns = [
        'Latitude', 'Longitude', 'Altitude',
        'Speed', 'Direction',
        'Accel_X', 'Accel_Y', 'Accel_Z'
    ]
    df = pd.DataFrame(data, columns=columns)
    df.to_csv(DATA_PATH, index=False)
    print(f"[✓] Data saved to {DATA_PATH}")

def main():
    data = generate_random_data(NUM_SAMPLES)
    save_data_to_csv(data)

if __name__ == '__main__':
    main()
