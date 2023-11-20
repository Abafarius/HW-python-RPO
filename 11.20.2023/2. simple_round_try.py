#Asking for float number from user
float_num_user = input("Enter float number:")

#Asking for count of numbers after comma from user
int_num_count_user = input("Enter count of numbers after comma (must be integer):")

#default values
def_float = 0.00729927007299270072992700729927
def_int = 2

try: 
    #Translating to float 
    float_num = float(float_num_user)
except ValueError:
    print("\nPlease, enter valid number. It must be float number. Now dafult value is active. \nfloat number:", def_float)
    float_num = def_float 

try:
    #Translating to int
    int_num_count = int(int_num_count_user)

except ValueError:
    print("\nYou didin't enter valid number. Now default value is active. \nnumbers after comma:",def_int,"\n")
    
    int_num_count = def_int

#Round function
round_fun = round(float_num, int_num_count)

#print result
print("Here is your rounded number:", round_fun)