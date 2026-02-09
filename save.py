import numpy as np
from data import *
from optimizing_pixels import  *

# Save full dataset
np.save("X_Train.npy", X_train)

# If you also have labels or masked maps la   ter:
# np.savez("dataset.npz", X=X_all, y=labels)
