# Exercise 1.2. Start the Python interpreter and use it as a calculator.

# 1. How many seconds are there in 42 minutes 42 seconds?
seconds = 42
minutes = 42
total_seconds = minutes * 60 + seconds
print('total_seconds: ', total_seconds)

# 2. How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
kilometers = 10
miles = kilometers / 1.61
print('miles: ', miles)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
#    mile in minutes and seconds)? What is your average speed in miles per hour?
time_per_mile_in_seconds = total_seconds / miles
print('average pace (seconds per mile): ', time_per_mile_in_seconds)
time_per_mile_in_minutes = time_per_mile_in_seconds / 60
print('average pace (minutes per mile): ', time_per_mile_in_minutes)
avg_speed_in_mph = 1 / time_per_mile_in_seconds * 60 * 60
print('average speed (mph): ', avg_speed_in_mph)

