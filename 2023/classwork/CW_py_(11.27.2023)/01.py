user_in = input("Enter No. of week:")
try:
    day = int(user_in)
except ValueError:
    print("value error")
    exit()

match day:
    case 1:
        day_name = "Monday"
    case 2:
        day_name = "Tuesday"   
    case 3:
        day_name = "Wednesday"
    case 4: 
        day_name = "Thursday"
    case 5:
        day_name = "Friday"
    case 6:
        day_name = "Saturday"   
    case 7:
        day_name = "Sunday"
    case _:
        day_name = "Unknown day"

    

day_name = ""
if day == 1:
    day_name = "Monday"
elif day == 2:  
    day_name = "Tuesday"
elif day == 3:
    day_name = "Wednesday"
elif day == 4:
    day_name = "Thursday"
elif day == 5:
    day_name = "Friday"
elif day == 6:
    day_name = "Saturday"
elif day == 7:
    day_name = "Sunday"
else:
    print("Unknown day")

print(day_name)