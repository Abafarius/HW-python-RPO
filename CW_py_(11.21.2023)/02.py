user_in = input("Enter your age: ")

try:
    age = int(user_in)
except ValueError:
    print("Enter valid number. It must be integer (0123456789).")
else:
    if age < 3:
        print("You are lying you can't be so young!")
    elif age > 120:
        print("You can't be so old. THat's impossible")
    else:
        print("wow cool you are", age, "years old")