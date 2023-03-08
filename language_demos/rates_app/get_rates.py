from datetime import date
import requests

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
    rate_responses.append(response)
  
  return rate_responses


def get_rates_threaded(start_date, end_date):
  ...

def get_rates_threadpool(start_date, end_date):
  ...

async def get_rates_async(start_date, end_date):
  ...


if __name__ == "__main__":
  print(get_rates_sync(date(2020, 1, 15), date(2020, 2, 10)))

