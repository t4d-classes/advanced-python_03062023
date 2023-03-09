from datetime import date
import requests
import threading
from concurrent.futures import ThreadPoolExecutor
import aiohttp
import asyncio

from business_days import business_days

# http://127.0.0.1:5050/api/2021-04-08?base=INR&symbols=USD,EUR

def get_rate_url(business_day):
  return (
    "http://127.0.0.1:5050"
    f"/api/{str(business_day)}"
    "?base=INR&symbols=USD,EUR"
  )

# get the data synchronously
def get_rates_sync(start_date, end_date):
  
  rate_responses = []

  for business_day in business_days(start_date, end_date):
    response = requests.get(get_rate_url(business_day), timeout=60)
    rate_responses.append(response.text)
  
  return rate_responses


def get_rate_thread(business_day, rate_responses):
    response = requests.get(get_rate_url(business_day), timeout=60)
    rate_responses.append(response.text)


def get_rates_thread(start_date, end_date):
    rate_responses = []
    threads: list[threading.Thread] = []

    for business_day in business_days(start_date, end_date):
        a_thread = threading.Thread(target=get_rate_thread, args=(business_day, rate_responses))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    return rate_responses


def get_rate_threadpool(business_day):
    response = requests.get(get_rate_url(business_day), timeout=60)
    return response.text


def get_rates_threadpool(start_date, end_date):
    with ThreadPoolExecutor(max_workers=20) as executor:
        return list(executor.map(
            get_rate_threadpool,
            list(business_days(start_date, end_date))
        ))
    
    
async def get_rate_async(session, business_day):
   async with session.get(get_rate_url(business_day)) as resp:
      return str(await resp.json())

async def get_rates_async(start_date, end_date):

    async with aiohttp.ClientSession() as session:
       return await asyncio.gather(*[
          get_rate_async(session, business_day)
          for business_day in business_days(start_date, end_date)
       ])



if __name__ == "__main__":
  print(get_rates_sync(date(2020, 1, 15), date(2020, 2, 10)))

