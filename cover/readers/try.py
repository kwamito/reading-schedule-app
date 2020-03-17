from datetime import date, datetime, timedelta

def today():
    month = date.today().month
    year = date.today().year
    day = date.today().day
    return date(year, month, day)

print(next_term())