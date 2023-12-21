#Бесконечный цикл, в котором повторятеся все операции программы до тех пор, пока не сработает break 
while True:
    #Ввод года
    user_Year = input("Enter your birth year: ")
    #Перехват ошибки значения
    try:
        year = int(user_Year)
    except ValueError:
        print('Wrong year')
        exit()


    #Ввод месяца
    user_Month = input("Enter your birth month: ")
    #Перехват ошибки значения
    try:
        month = int(user_Month)
    except ValueError:
        print('Wrong month')
        exit()


    #Ввод дня
    user_Day = input("Enter your birth day: ")
    #Перехват ошибки значения и перевод со строки в целочисленный тип данных
    try:
        day = int(user_Day)
    except ValueError:
        print('Wrong day')
        exit()



    #проверка правильности месяца, какой месяц с 31ым ли днем, проверка дня лежит ли в диапазоне, также проверка адекватности года
    if (0<=month<=12) and (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and (0<=day<=31) and (1900<=year<=2023):
            #Перевод обратно в строки
            string_Month = str(month)
            string_Day = str(day)
            string_Year = str(year)
            #Подстановка значений
            formated = "%s.%s.%s" % (string_Day, string_Month, user_Year)
            #Вывод результата
            print("dd.mm.yyy format:", formated)
            #Выход из цикла
            break
    #Вывод ошибки в случае неправильности условия выше
    else:
         print("\nsomething went wrong try again (day, month or year wrong, days must be at most 31)\n")

    #проверка правильности месяца, какой месяц с 30ым ли днем, проверка дня лежит ли в диапазоне, также проверка адекватности года
    if (0<=month<=12) and (month == 4 or month == 6 or month == 9 or month == 11) and (0<=day<=30) and (1900<=year<=2023):
            #Перевод обратно в строки
            string_Month = str(month)
            string_Day = str(day)
            string_Year = str(year)
            #Подстановка значений
            formated = "%s.%s.%s" % (string_Day, string_Month, user_Year)
            #Вывод результата
            print("dd.mm.yyy format:", formated)
            #Выход из цикла
            break
    #Вывод ошибки в случае невыполниения условия выше
    else:
         print("\nsomething went wrong try again (day, month or year wrong, days must be at most 30)\n")

    #Проверка месяца и адекватность года
    if (0<=month<=12) and (month == 2) and (1900<=year<=2023):
        #Проверка на високосный год
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            #Проверка диапазона дней
            if 0<=day<=29:
                #Перевод обратно в строки
                string_Month = str(month)
                string_Day = str(day)
                string_Year = str(year)
                #Подстановка значений
                formated = "%s.%s.%s" % (user_Day, string_Month, user_Year)
                #Вывод результата
                print("dd.mm.yyy format:", formated)
                #Выход из цикла
                break
            #Вывод ошибки выхода из диапазона дней
            else:
                print("day must be in range 0-29")
        #Ну значит не вискосный год                
        else:
            #Проверка диапазона дней 
            if 0<=day<=28:
                #Перевод обратно в строки
                string_Month = str(month)
                string_Day = str(day)
                string_Year = str(year)
                #Подстановка значений
                formated = "%s.%s.%s" % (user_Day, string_Month, user_Year)
                #Вывод результата
                print("dd.mm.yyy format:", formated)
                #Выход из цикла
                break
            #Вывод ошибки выхода из диапазона дней
            else:
                 print("day must be in range 0-28")
    #Неправильный месяц или год
    else:
         print("\nWrong month or year, please try again\n")
#Думаю со списками было бы поменьше кода


"""VN: Ну вы прям заморочились)))
А правильный формат дд.мм.гггг не реализовали:

Enter your birth year: 1981
Enter your birth month: 4
Enter your birth day: 2

something went wrong try again (day, month or year wrong, days must be at most 31)

dd.mm.yyy format: 2.4.1981


Должно быть: 02.04.1981
И 'something went wrong...' , хотя данные корректные
"""
#AS: Я примерно понял как делать, нужно подстановкой сделать, поставить спереди %s 0. Я так понимаю нужно сделать дополнительные условия, вроде того если цифра дня или месяца меньше 10 то сделать так, а в ином случае оставить так.
#VN: метка %02d решает все проблемы сама