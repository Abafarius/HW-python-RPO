x1 = input("Enter 1st x dot: ")
x2 = input("Enter 2st x dot: ")
y1 = input("Enter 1nd y dot: ")
y2 = input("Enter 2nd y dot: ")
str_to_int_x1 = int(x1)
str_to_int_x2 = int(x2)
str_to_int_y1 = int(y1)
str_to_int_y2 = int(y2)
distance_dots = ((str_to_int_x1-str_to_int_x2)**2+(str_to_int_y1-str_to_int_y2)**2)**0.5
#VN: очень сложно читаемое выражение. Можно попробовать поиграть названиями переменных так, чтобы в итоге легко читалось
print("distance between dots: ", distance_dots)
