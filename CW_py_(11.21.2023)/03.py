user_in_hour = input("Enter hour:")
user_in_minute = input("Enter minutes:")
user_in_second = input("Enter seconds:")

try:
    hour = int(user_in_hour)
except ValueError:
    print("Enter valid number!")
else:
    try:
        minute = int(user_in_minute)
    except ValueError:
        print("Enter valid number!")
    else:
        try:
            second = int(user_in_second)
        except ValueError:
             print("Enter valid number!")
        else:
            if hour > 23 and hour < 0:
                print("Hours can't be bigger 23 and can't be lower than 0")
            elif minute > 60 and minute < 0:
                print("Minutes can't be bigger 60 and can't be lower than 0")
            elif second > 60 and second < 0:
                print("Minutes can't be bigger 60 and can't be lower than 0")
            else:
                print("So you entered:", hour, "hours", minute, "minutes and", second, "seconds")


