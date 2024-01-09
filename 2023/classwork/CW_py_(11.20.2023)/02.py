user_input = input("Enter radius of circle:")
pi = 3.14
try:
    r = int(user_input)
except ValueError:
    print("Enter valid number")
else:
    area = pi*r**2
    print("The area of circle:", area)