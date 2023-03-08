from contextlib import contextmanager
import multiprocessing as mp

import requests
from requests.exceptions import RequestException

from rates_api import start_rates_api


@contextmanager
def rates_api_server(health_check_url):
    
    rates_api_process = mp.Process(target=start_rates_api)
    rates_api_process.start()

    while True:
        
        try:
            requests.get(health_check_url, timeout=2)
            break
        except ConnectionError:
            continue
        except RequestException:
            continue

    yield # transfer control back the with block

    # run when we exit the with block
    rates_api_process.terminate()
