length_user = input("Enter length  of string: ")

try:
    length = int(length_user)
except ValueError:
    print("Error!")
    exit()

givenChars = "C1 C2 " * length
print(givenChars)