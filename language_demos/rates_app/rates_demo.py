from datetime import date
import time

from rates_api_server import rates_api_server
from get_rates import get_rates_sync

if __name__ == "__main__":
    
    health_check_url = "http://localhost:5050/check"

    with rates_api_server(health_check_url):
        start_time = time.time()
        resp_len = len(get_rates_sync(date(2020, 1, 15), date(2020, 2, 10)))
        print(f"get_rates_sync responses length: {resp_len}")
        end_time = time.time()
        print(f"get_rates_sync: {end_time-start_time}")

