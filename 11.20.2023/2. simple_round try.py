#Asking for float number from user
float_num_user = input("Enter float number:")

#Asking for count of numbers after comma from user
int_num_count_user = int(input("Enter count of numbers after comma (must be integer):"))

#Translating to float 
float_num = float(float_num_user)

#Translating to int
int_num_count = int(int_num_count_user)

#Round function
round_fun = round(float_num, int_num_count)

#print result
print("Here is your rounded number:", round_fun)