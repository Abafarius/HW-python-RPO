#Asking for numbers from user
user_a_num = input("Enter <a> number:")
user_b_num = input("Enter <b> number:")

def_num_a = 137
def_num_b = 1
def_num_x = -0.0072992700729927005

#Translating user data to integer
try:
    a = int(user_a_num)
except ValueError:
    print("\nEnter valid number. Now default a value is active:", def_num_a)
    a = def_num_a

try: 
    b = int(user_b_num)
except ValueError:
    print("Enter valid number. Now default b value is active:", def_num_b, "\n")
    b = def_num_b

try:
    #Calculating x
    x = -b/a
except ZeroDivisionError:
    print("Number a can't be zero, we can't divide to zero. Anyway default x num is:", x)
    x = def_num_x

#print result
print("Here is you x number:", x)
