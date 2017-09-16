"""This file runs scraper hourly. Keep open on server."""
import scrape
import time

# Seconds in an hour.
TIME_INTERVAL = 216000

if __name__ == "__main__":
    main

@shared_task
def main():
    while True:
        scrape.run_scraper()
        time.sleep(TIME_INTERVAL)
