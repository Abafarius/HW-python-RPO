#Asking for numbers
user_hour_num = input("Enter a current hour time:")
user_minute_num = input("Enter a current minute time:")

#declaring constants 
hour_const = 23
minute_const = 60

#Translating user data to integer
try: 
    hour = int(user_hour_num)
except: 
    print("\nYou entered wrong value for hour. Please, enter integer number from 0 to 23. Now default value is active:", hour_const)
    hour = hour_const

try:
    minute = int(user_minute_num)
except:
    print("You entered wrong value for minute. Please, enter integer number from 0 to 60. Now default value is active:", minute_const, "\n")
    minute = minute_const

#Calculating hours and minutes until end of a day
calculation_hour = abs(hour_const-hour)
calculation_minute = abs(minute_const-minute)

#print result
print("There's still", calculation_hour,"hours and", calculation_minute,"minute untill tomorrow")