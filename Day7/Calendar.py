"""https://www.hackerrank.com/challenges/calendar-module/problem"""

"""The calendar module allows you to output calendars and provides additional useful functions for them."""
import calendar
month1, day, year = list(map(int,input().split()))
day1 = calendar.weekday(year, month1, day)
print((calendar.day_name[day1].upper()))