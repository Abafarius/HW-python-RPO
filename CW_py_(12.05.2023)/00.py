user_in = input("Enter numbers with spaces: ")
user_list = user_in.split(" ")

'''
numbers = []
print(user_list)
for i in user_list:
    numbers.append(int(i))
print(numbers)
'''
print(user_list)
for i in range(len(user_list)):
    user_list[i] = int(user_list[i])
print(user_list)