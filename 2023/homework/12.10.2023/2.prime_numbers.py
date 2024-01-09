source = input("Enter numbers by space: ")
source_list = source.split(' ')

numbers = []
try:
    for x in source_list:
        numbers += [int(x)]
except ValueError:
    print("All entered data must be integer numbers")
    exit()

print(numbers)
is_simple = True
result = []
for x in numbers:
    if x <= 0:
        continue
    elif x > 1:
        is_simple = True
        for i in range(2, 1 + x//2):
            if x % i == 0:
                is_simple = False
                break
    if is_simple:
        result.append(x)

print(result)
