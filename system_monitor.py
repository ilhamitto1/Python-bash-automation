#!/usr/bin/env python3
import psutil
import datetime
import time
import argparse

def log_system_usage(output_file):
    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    line = f"{time_now} | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%\n"
    with open(output_file, "a") as f:
        f.write(line)
    print(line.strip())

def main(count, interval, output):
    for _ in range(count):
        log_system_usage(output)
        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple system monitor")
    parser.add_argument("--count", type=int, default=5, help="Number of measurements")
    parser.add_argument("--interval", type=int, default=1, help="Seconds between measurements")
    parser.add_argument("--output", type=str, default="system_log.txt", help="Output log file")
    args = parser.parse_args()
    main(args.count, args.interval, args.output)
