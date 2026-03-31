import pandas as pd

class LapPreprocessor:
    def __init__(self, laps):
        self.laps = laps

    def filter_laps(self, laps):
        laps = laps.dropna(subset=['LapTime'])
        laps = laps[pd.isnull(laps['PitOutTime'])]
        laps = laps[pd.isnull(laps['PitInTime'])]
        laps = laps[laps['LapNumber'] > 1]
        return laps.reset_index(drop=True)

    def label_laps(self, laps):
        laps = laps.copy()
        laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()
        Q1 = laps['LapTimeSeconds'].quantile(0.25)
        Q3 = laps['LapTimeSeconds'].quantile(0.75)
        IQR = Q3 - Q1
        laps['is_anomaly'] = laps['LapTimeSeconds'] > (Q3 + 1.5 * IQR)
        return laps

    def normalize_signal(self, series):
        min_val = series.min()
        max_val = series.max()
        if max_val == min_val:
            return series * 0.0
        return (series - min_val) / (max_val - min_val)