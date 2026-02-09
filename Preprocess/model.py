import tensorflow as tf
from tensorflow.keras import layers, models

T = 57
C = 5

model = models.Sequential([
    layers.Input(shape=(T, C)),

    layers.LSTM(64, return_sequences=True),
    layers.LSTM(32, return_sequences=False),

    layers.RepeatVector(T),

    layers.LSTM(32, return_sequences=True),
    layers.LSTM(64, return_sequences=True),

    layers.TimeDistributed(layers.Dense(C))
])

model.compile(
    optimizer='adam',
    loss='mse'
)

model.summary()
