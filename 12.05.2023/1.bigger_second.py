list_num = [3, 9, 8, 4, 5, 1]
length_list = len(list_num)
for i in range(length_list):
    try:
        if list_num[i] < list_num[i+1]:
            print(list_num[i+1])
    except IndexError:
        print("Oh well... your list is end up")
        exit()
    