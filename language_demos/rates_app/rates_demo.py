from datetime import date
import time

from rates_api_server import rates_api_server
from get_rates import get_rates_sync, get_rates_thread, get_rates_threadpool

if __name__ == "__main__":
    
    health_check_url = "http://localhost:5050/check"

    with rates_api_server(health_check_url):

        start_time = time.time()
        resp = get_rates_sync(date(2020, 1, 15), date(2020, 2, 10))
        #print(f"get_rates_sync responses length: {resp_len}")
        end_time = time.time()
        print(f"get_rates_sync: {end_time-start_time}")
        for r in resp:
            print(r)

        start_time = time.time()
        resp = get_rates_thread(date(2020, 1, 15), date(2020, 2, 10))
        #print(f"get_rates_thread responses length: {resp_len}")
        end_time = time.time()
        print(f"get_rates_thread: {end_time-start_time}")
        for r in resp:
            print(r)

        start_time = time.time()
        resp = get_rates_threadpool(date(2020, 1, 15), date(2020, 2, 10))
        #print(f"get_rates_threadpool responses length: {resp_len}")
        end_time = time.time()
        print(f"get_rates_threadpool: {end_time-start_time}")        
        for r in resp:
            print(r)
