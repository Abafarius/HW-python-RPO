user_hour_num = input("Enter a current hour time:")
user_minute_num = input("Enter a current minute time:")

hour_const = 23
minute_const = 60

hour = int(user_hour_num)
minute = int(user_minute_num)

calculation_hour = abs(hour_const-hour)
calculation_minute = abs(minute_const-minute)

print("There's still", calculation_hour,"hours and", calculation_minute,"minute untill tomorrow")