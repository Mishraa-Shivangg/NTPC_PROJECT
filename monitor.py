import csv
import time
from datetime import datetime
from ping3 import ping, errors
import pandas as pd
import schedule
import os

devices = pd.read_csv('devices.csv')
downtime_log = 'downtime_log.csv'

if not os.path.isfile(downtime_log):
    with open(downtime_log, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'device', 'ip_address', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

def check_availability():
    with open(downtime_log, 'a', newline='') as csvfile:
        fieldnames = ['timestamp', 'device', 'ip_address', 'status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        for _, row in devices.iterrows():
            ip = row['ip_address']
            name = row['name']
            status = "down"   # assume down by default

            try:
                # Try 3 pings, each with 2 sec timeout
                success_count = 0
                for _ in range(5):
                    resp = ping(ip, timeout=2, unit='ms')
                    if resp is not None and isinstance(resp, (int, float)) and resp > 0:
                        success_count += 1

                if success_count > 0:
                    status = "up"

            except errors.PingError:
                status = "down"
            except Exception:
                status = "down"

            writer.writerow({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'device': name,
                'ip_address': ip,
                'status': status
            })
            csvfile.flush()

# Run every 10 seconds
schedule.every(10).seconds.do(check_availability)

while True:
    schedule.run_pending()
    time.sleep(1)

