from model import model
from optimizing_pixels import X_train

history = model.fit(
    X_train,
    X_train,
    epochs=20,
    batch_size=256,
    validation_split=0.1
)
