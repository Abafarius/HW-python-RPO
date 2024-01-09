list_num1 = [11, 9, 15, 2, 5, 1]
list_num_temp = []
list_num2 = [1, 8, 9, 5, 4, 3, 6]
for i in list_num1:
    if i not in list_num2:
        list_num_temp.append(i)
list_num1 = list_num_temp
print(list_num1)
