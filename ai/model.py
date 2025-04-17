import tensorflow as tf
from tensorflow.keras import layers, models

def build_model(input_shape=(4,), output_shape=3):
    """
    یک مدل ساده MLP برای کنترل کوادکوپتر
    - input_shape: اطلاعات حالت مجازی شبیه‌ساز (مثلاً x, y, z, angle)
    - output_shape: تعداد اکشن‌ها (مثلاً جلو، چپ، راست)
    """
    model = models.Sequential([
        layers.Input(shape=input_shape),
        layers.Dense(64, activation='relu'),
        layers.Dense(64, activation='relu'),
        layers.Dense(output_shape, activation='linear')  # مقدار کنترل برای هر محور
    ])

    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
        loss='mse',
        metrics=['mae']
    )

    return model
