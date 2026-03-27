import fastf1
import os

class F1DataCollector:

    def __init__(self,cache_dir=None):
        self.cache_dir = cache_dir or os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'raw')
        os.makedirs(self.cache_dir, exist_ok=True)
        fastf1.Cache.enable_cache(self.cache_dir)

    def load_session(self, year, race_name, session_name='R'):
        self.session = fastf1.get_session(year, race_name, session_name)
        self.session.load(telemetry=True)

    def get_laps(self, driver_code):
        lap = self.session.laps.pick_driver(driver_code)
        return lap
    
    def get_telemetry(self, lap):
        return lap.get_car_data().add_distance()

