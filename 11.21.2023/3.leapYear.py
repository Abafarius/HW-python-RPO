ud = input("Enter year:")

try:
    year = int(ud)
except ValueError:
    print("Value error just occured! You must type integer number!")

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else: 
    print("not leap year")


'''
else:
    if 0<=year<=2100:
        if year % 4 == 0:
            if year % 100 ==0:
                if year % 400 == 0:
                    print("leap year")
                else:
                    print("not leap year")
            else:
                print("leap year")
        else: 
            print("It's not a leap year")
    else:
        print("I don't want to calculate the far future or the far past")
'''


#VN: Всё ж намного проще можно. Сама структура выражения уже содержится в условии задачи:
# year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
#AS: Действительно все проще чем казалось. Я просто условие задачи неправильно понял, я первые два условия вместе взял, а последнее отдельно сделал, поэтому в одной строке не получалось, потом мне пришлось залезть в гугл, а там нашел интересный алгоритм от майкрософт и воспроизвел его в код =D 