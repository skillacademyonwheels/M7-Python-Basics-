import datetime as dt

current_time = dt.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current Date and Time: {formatted_time}")


### Print calender for the current year
import calendar

year = calendar.calendar(2025)c
print(f"Calendar for the year 2025:\n{year}")