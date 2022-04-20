# Вариант №1
# duration = input('Please enter the number of seconds: ')
# num_seconds = int(duration)
# num_day = num_seconds // 86400
# num_seconds %= 86400
# num_hour = num_seconds // 3600
# num_seconds %= 3600
# num_minute = num_seconds // 60
# num_seconds %= 60
# print(num_day, 'days', num_hour, 'hours', num_minute, 'minutes', num_seconds, 'seconds')


# Вариант №2
duration = input('Please enter the number of seconds: ')
num_seconds = int(duration)
num_day = num_seconds // 86400
num_hour = (num_seconds - (num_day * 86400)) // 3600
num_minute = (num_seconds - ((num_day * 86400) + (num_hour * 3600))) // 60
num_seconds = num_seconds - ((num_day * 86400) + (num_hour * 3600) + (num_minute * 60))
print(num_day, 'days', num_hour, 'hours', num_minute, 'minutes', num_seconds, 'seconds')
