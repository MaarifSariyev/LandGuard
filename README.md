# 🌍 LandGuard — AI-Powered Land Change Detection Using Sentinel Time Series

LandGuard is an AI-driven geospatial monitoring system that automatically detects land-use and urban changes using multi-temporal Sentinel-1 & Sentinel-2 satellite imagery.

The system leverages an LSTM Autoencoder trained on pixel-level time series to identify anomalous patterns such as:

- Unauthorized construction  
- Vegetation loss  
- Soil-to-building transitions  
- Road development  
- Urban expansion  

Designed for scalable city-wide monitoring with minimal computational cost.

---

## 🚀 Key Features

- Multi-sensor fusion (Sentinel-1 SAR + Sentinel-2 Optical)
- Pixel-level time series modeling
- LSTM Autoencoder for unsupervised anomaly detection
- Reconstruction-error based change scoring
- Geospatial anomaly mapping (QGIS compatible)
- Designed for large-scale deployment (millions of pixels)

---

## 🛰 Data Sources

- Sentinel-1 (VV, VH)
- Sentinel-2 (B4, B8)
- Derived indices:
  - NDVI (vegetation)
  - NDBI (built-up)

Spatial resolution: **10 meters**

Temporal depth: **57 timesteps**

---

## 🧠 Model Architecture

LSTM Autoencoder:
Input (57×5)
→ LSTM(64)
→ LSTM(32)
→ Dense(32)
→ RepeatVector
→ LSTM(32)
→ LSTM(64)
→ TimeDistributed(Dense(5))


Loss: Mean Squared Error (MSE)

Framework: TensorFlow / Keras

Purpose: Learn normal temporal behavior and flag deviations via reconstruction error.

---

## 📊 Pipeline Overview

1. Export Sentinel imagery via Google Earth Engine
2. Convert GeoTIFF tiles into pixel-level time series
3. Normalize and store as `.npy`
4. Train LSTM Autoencoder
5. Compute reconstruction error per pixel
6. Flag anomalies using percentile threshold (p99.9)
7. Map flagged pixels back to geographic coordinates
8. Visualize results in QGIS / Google Earth

---

## 📈 Results

- Dataset size: ~7.4 million pixels
- Detected anomalies: ~7,000 high-risk locations
- Manual geospatial validation shows approximately **75–85% precision**
- System automatically filters over **99% of stable areas**

This dramatically reduces manual inspection effort for urban monitoring.

---

## 🗺 Geospatial Output

Each detected anomaly includes:

- Global pixel index
- Source GeoTIFF tile
- Row / column
- Latitude / longitude
- Reconstruction error score

Exported as:

flagged_idx.csv

Compatible with QGIS and other GIS platforms.

---

## 🛠 Tech Stack

- Google Earth Engine
- Python
- NumPy
- Rasterio
- TensorFlow / Keras
- QGIS
- Google Colab

---

## 🎯 Use Cases

- Smart city monitoring
- Illegal construction detection
- Environmental protection
- Infrastructure development tracking
- Municipal planning

---

## 👥 Team

- **Maarif Sariyev** — AI Engineer / Model Development  
- **Ilahe** — Data Scientist  
- **Nezrin** — Software Developer
---

## 📬 Contact

For collaboration or inquiries:

Maarif Sariyev  
AI Engineer  
📧 maarifsariyev5@gmail.com
