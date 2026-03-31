import numpy as np

class TelemetryImager:
    def __init__(self, n_bins=200):
        self.n_bins = n_bins

    def lap_to_image(self, telemetry, preprocessor):
        signals = ['Speed', 'Throttle', 'Brake', 'nGear', 'RPM']

        grid = np.linspace(telemetry['Distance'].min(), telemetry['Distance'].max(), self.n_bins)

        rows = []
        for signal in signals:
            normalized = preprocessor.normalize_signal(telemetry[signal].astype(float))
            interpolated = np.interp(grid, telemetry['Distance'], normalized)
            rows.append(interpolated)

        return np.stack(rows)  # shape: (5, n_bins)
        
        
        