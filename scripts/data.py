import argparse
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import fastf1
from tqdm import tqdm
from src.data.collector import F1DataCollector

def main():
    parser = argparse.ArgumentParser(description='Bulk download F1 telemetry data')
    parser.add_argument('--year', type=int, action='append', dest='years', required=True)
    args = parser.parse_args()

    for year in args.years:
        schedule = fastf1.get_event_schedule(year)
        schedule = schedule[schedule['RoundNumber'] > 0]

        for _, row in tqdm(schedule.iterrows(), total=len(schedule), desc=f"Downloading {year}"):
            try:
                collector = F1DataCollector()
                collector.load_session(year, row['EventName'])
                print(f"  ✓ {year} {row['EventName']}")
            except Exception as e:
                print(f"  ✗ {year} {row['EventName']}: {e}")


if __name__ == '__main__':
    main()
        
