#Asking for numbers
user_hour_num = input("Enter a current hour time:")
user_minute_num = input("Enter a current minute time:")

#declaring constants 
hour_const = 23
minute_const = 60

#Translating user data to integer
hour = int(user_hour_num)
minute = int(user_minute_num)

#Calculating hours and minutes until end of a day
calculation_hour = abs(hour_const-hour)
calculation_minute = abs(minute_const-minute)

#print result
print("There's still", calculation_hour,"hours and", calculation_minute,"minute untill tomorrow")