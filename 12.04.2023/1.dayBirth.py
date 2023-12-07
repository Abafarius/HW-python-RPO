user_Year = input("Enter your birth year: ")
user_Month = input("Enter your birth month: ")
user_Day = input("Enter your birth day: ")

try:
    year = int(user_Year)
except ValueError:
    print('Wrong year')
    exit()
try:
    month = int(user_Month)
except ValueError:
    print('Wrong month')
    exit()
try:
    day = int(user_Day)
except ValueError:
    print('Wrong day')
    exit()

if (0<=month<=12):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if 0<=day<=31:
            string_Month = str(month)
            formated = "%s.%s.%s" % (user_Day, string_Month, user_Year)
            print("dd.mm.yyy format:", formated)
        else:
            print("day must be in range 0-31")
    elif month == 2:
        


else:
    print("There's only 12 months and it can't be negative!")


