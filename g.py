from datetime import date, time, datetime
# date(year=2000, month=1, day=31)
# time(hour=13, minute=14, second=31)
# datetime(year=2000, month=1, day=31, hour=13, minute=14, second=31)

# today=date.today()
# now=datetime.now()
# current_time=time(now.hour,now.minute, now.second)
# datetime.combine(today, current_time)
# print(current_time, today)

# date_string="01-31-2020 14:45:37"
# format_string= "%m-%d-%Y %H:%M%S"
# datetime.strptime(date_string, format_string)

# from datetime import datetime, timedelta
# now=datetime.now()
# now
# tomorrow=timedelta(days=+1)
# now+tomorrow
# print(now+tomorrow)

birthday= (input("Enter your birthdate(YYYY-MM-DD): "))
birth_date=datetime.strptime(birthday, "%Y-%m-%d")
today=datetime.today()
age=today.year-birth_date.year
print(age)
