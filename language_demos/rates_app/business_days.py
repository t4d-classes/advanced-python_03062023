from datetime import date, timedelta
import holidays

def business_days(start_date, end_date):

    us_holidays = holidays.UnitedStates()

    for day in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            yield the_date

def business_days_list(start_date, end_date):

    us_holidays = holidays.UnitedStates()

    days = []

    for day in range((end_date - start_date).days + 1):
        the_date = start_date + timedelta(day)
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days


if __name__ == "__main__":
    for business_day in business_days(date(2023, 2, 14), date(2023, 3, 17)):
        print(business_day)        
