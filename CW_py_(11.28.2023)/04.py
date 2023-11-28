user_num = input("Enter number: ")

try:
    num = int(user_num)

except ValueError:
    print("Value Error!")

for i in range(1,9):
    if num%i == 0:
        print(i)