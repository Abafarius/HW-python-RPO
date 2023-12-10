user_num = input("Enter number: ")

try:
    num = int(user_num)

except ValueError:
    print("Value Error!")
#VN: нужно либо exit() в случае исключения, либо всё что ниже в блок else вложить. Иначе try бесполезен
# Эта проблема и в других задачах тоже
for i in range(1,num):
    if num%i == 0:
        print(i)