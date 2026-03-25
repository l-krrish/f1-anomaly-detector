# F1 Anomaly Detector

An end-to-end ML project that detects anomalous laps in Formula 1 telemetry data using a custom VGG-style CNN trained on 2D heatmap images derived from raw telemetry signals.

## Project Structure

```
f1-anomaly-detector/
├── data/
│   ├── raw/            # FastF1 cache (auto-populated by collector)
│   └── processed/      # Extracted features, labels, and images
├── notebooks/
│   ├── day1_eda.ipynb              # EDA across 2023–2024 seasons
│   └── day2_feature_engineering.ipynb  # Imaging + labeling pipeline
├── src/
│   ├── data/
│   │   ├── collector.py    # FastF1 data download & cache management
│   │   └── preprocessor.py # Lap filtering, normalization
│   ├── features/
│   │   ├── engineer.py     # Feature extraction from raw telemetry
│   │   └── imaging.py      # Convert telemetry → 2D heatmap images
│   ├── models/
│   │   └── vgg_cnn.py      # VGG-style CNN in PyTorch
│   └── visualization/
│       └── plots.py        # Shared plotting utilities
├── train/
│   └── train.py            # Training loop with curves
├── app/
│   ├── app.py              # Flask dashboard
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── styles.css
├── scripts/
│   └── collect_data.py     # CLI script to bulk-download data
├── Dockerfile
└── requirements.txt
```

## 5-Day Plan

| Day | Focus | Key Output |
|-----|-------|------------|
| 1 | Data Collection & EDA | FastF1 telemetry for all 2023–2024 races |
| 2 | Feature Engineering | Telemetry heatmap images + anomaly labels |
| 3 | VGG-style CNN | Trained model + training curves (Kaggle GPU) |
| 4 | Flask Dashboard | Web UI with anomaly scores per driver/race |
| 5 | Deploy on HF Spaces | Docker container live on Hugging Face |

## Setup

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Collect data (takes ~20–30 min first run due to caching)
python scripts/collect_data.py --year 2023 --year 2024

# Run the Flask dashboard
python app/app.py
```

## How It Works

1. **Data**: FastF1 pulls official F1 timing + telemetry (speed, throttle, brake, gear, RPM) per lap per driver
2. **Imaging**: Each lap's multi-channel telemetry is resampled to a fixed distance grid and encoded as a 2D heatmap (channels × distance_bins) image
3. **Labels**: Anomalous laps are labeled using IQR-based outlier detection on lap time residuals (after controlling for compound and track evolution)
4. **Model**: A VGG-style CNN classifies each telemetry image as normal or anomalous
5. **Dashboard**: Flask app renders per-driver anomaly scores, flagged lap plots, and race selectors

## Deploy to HF Spaces

```bash
docker build -t f1-anomaly-detector .
# Push to Hugging Face Spaces via git or CLI
```
