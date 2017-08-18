"""This file runs scraper hourly. Keep open on server."""
import scraper
import time

# Seconds in an hour.
TIME_INTERVAL = 216000

if __name__ == "__main__":
    while True:
        scraper.run_scraper()
        time.sleep(TIME_INTERVAL)
