while True:
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

    if (0<=month<=12) and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (0<=day<=31) and (1900<=year<=2023):
            string_Month = str(month)
            string_Day = str(day)
            string_Year = str(year)
            formated = "%s.%s.%s" % (string_Day, string_Month, user_Year)
            print("dd.mm.yyy format:", formated)
            break
    else:
         print("\nsomething went wrong try again (day, month or year wrong, days must be at most 31)\n")

    if (0<=month<=12) and (month == 4 or month == 6 or month == 9 or month == 11) and (0<=day<=30) and (1900<=year<=2023): 
            string_Month = str(month)
            string_Day = str(day)
            string_Year = str(year)
            formated = "%s.%s.%s" % (string_Day, string_Month, user_Year)
            print("dd.mm.yyy format:", formated)
            break
    else:
         print("\nsomething went wrong try again (day, month or year wrong, days must be at most 30)\n")

    if (0<=month<=12) and (month == 2) and (1900<=year<=2023):
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            if 0<=day<=29:
                string_Month = str(month)
                string_Day = str(day)
                string_Year = str(year)
                formated = "%s.%s.%s" % (user_Day, string_Month, user_Year)
                print("dd.mm.yyy format:", formated)
                break
            else:
                print("day must be in range 0-29")                
        else: 
            if 0<=day<=28:
                string_Month = str(month)
                string_Day = str(day)
                string_Year = str(year)
                formated = "%s.%s.%s" % (user_Day, string_Month, user_Year)
                print("dd.mm.yyy format:", formated)
                break
            else:
                 print("day must be in range 0-28")
    else:
         print("\nWrong month or year, please try again\n")
#Думаю со списками было бы поменьше кода


