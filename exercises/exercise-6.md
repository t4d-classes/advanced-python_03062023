# Exercise 6

0. Create a new folder named `rates_app` in the `language_demos` folder.

1. Create a new Python file named `business_days.py` in the `rates_app` folder. Do all coding for the exercise in the `business_days.py` file.

2. Create a function named "business_days" that returns the business days between a start date and an end date. The date range should be inclusive of the start and end date. Use a generator to implement the function.

3. A business day is defined as any date that is not a weekend or a US holiday. Explore the "holidays" package on PyPi.org to figure out how to determine US holidays.

Note: if Conda does not work, try `pip`: https://pypi.org/project/holidays/
```
pip install holidays
```

4. Using the "business_days" function display a listing of all business days between the start and end date in the console. Please display one date per line.