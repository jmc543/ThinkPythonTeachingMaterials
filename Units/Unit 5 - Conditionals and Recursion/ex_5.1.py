# solution to exercise 5.1 of Think Python.

import time

# current time in seconds since January 1st, 1970:
epoch = time.time()

seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

days = epoch // seconds_in_a_day

seconds_to_midnight_today = days * seconds_in_a_day
seconds_since_midnight_today = epoch - seconds_to_midnight_today

hours = seconds_since_midnight_today // seconds_in_an_hour

minutes = (seconds_since_midnight_today - (hours * seconds_in_an_hour)) // seconds_in_a_minute

seconds = seconds_since_midnight_today - (hours * seconds_in_an_hour + minutes * seconds_in_a_minute)

print("In GMT: ", hours, " hours,", minutes, " minutes,", seconds, " seconds, and ", days, " days since the epoch")

