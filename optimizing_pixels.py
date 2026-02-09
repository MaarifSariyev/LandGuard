import numpy as np
from data import X_all

num_pixels = X_all.shape[0]
sample_size = 100_000

idx = np.random.choice(num_pixels, sample_size, replace=False)
X_train = X_all[idx]

print(X_train.shape)
# (100000, 57, 5)
 