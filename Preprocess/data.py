import rasterio
import numpy as np

# ds = rasterio.open("Baku_Sentinel_TimeSeries-0000000000-0000000000.tif")
# data = ds.read()  # (bands, H, W)
#
# bands, H, W = data.shape
# C = 5
# T = bands // C
#
# # (bands, H, W) → (C, T, H*W) → (pixels, T, C)
# X = data.reshape(C, T, H * W).transpose(2, 1, 0)
#
# print(X.shape)
# # (num_pixels, T, C)
import glob

all_samples = []

for tif in glob.glob("Baku_Sentinel_TimeSeries-*.tif"):
    ds = rasterio.open(tif)
    data = ds.read()

    bands, H, W = data.shape
    C = 5
    T = bands // C

    X = data.reshape(C, T, H * W).transpose(2, 1, 0)
    all_samples.append(X)

X_all = np.concatenate(all_samples, axis=0)

print(X_all.shape)
# (TOTAL_PIXELS, T, C)
