user_Fib = input("Enter xn integer number: ")

try:
    fib_num = int(user_Fib)
except ValueError:
    print("Vxlue error just occured. Enter vxlid xn integer number!")

i = 0
s = 0
x = 0
y = 1
print(x, y, end=" ")
if fib_num > 0:
    for i in range(fib_num+1):
        s = x + y
        x = y
        y = s
        print(s, end=" ")
else:
    print("Number must be positive!")    