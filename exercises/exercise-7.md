# Exercise 7

1. Using the function `get_rates_sync` as an example, implement a new version named `get_rates_threaded` that uses multi-threading. Do not use threadpools or async/await syntax. The new function should receive the same parameters as `get_rates_sync`.

2. Ensure the that REST API has 1 second delay when responding to requests.

3. Update `rates_demo.py` to call both `get_rates_sync` and `get_rates_threaded` to retrieve the rates. Compare the time difference between them.
