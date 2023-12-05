user_list =[]
new_list = []
while len(user_list) != 10:
    user_in = input("Enter numbers with spaces: ")
    user_list = user_in.split(" ")
    user_list = user_list[:10]

print(user_list)