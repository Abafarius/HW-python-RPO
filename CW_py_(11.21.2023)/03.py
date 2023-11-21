user_in_hour = input("Enter hour:")
user_in_minute = input("Enter minutes:")
user_in_second = input("Enter seconds:")

try:
    hour = int(user_in_hour)
except ValueError:
    print("Enter valid hour number!")
else:
    try:
        minute = int(user_in_minute)
    except ValueError:
        print("Enter valid minute number!")
    else:
        try:
            second = int(user_in_second)
        except ValueError:
             print("Enter valid seconds number!")
        else:
            if hour > 23 or hour < 0:
                print("Hours can't be bigger 23 and can't be lower than 0")
            elif minute > 60 or minute < 0:
                print("Minutes can't be bigger 60 and can't be lower than 0")
            elif second > 60 or second < 0:
                print("seconds can't be bigger 60 and can't be lower than 0")
            else:
                print("So you entered:", hour, "hours", minute, "minutes and", second, "seconds")


