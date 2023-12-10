un = input("Enter number: ")

max_digit = "0"
min_digit = "9"


j = 0
for i in un:

    if un[j] >= max_digit:
    #VN: вместо un[j] спокойно можно использовать i, ведь у вас цикл перебирает символы из un
        max_digit = un[j]

        
    if un[j] <= min_digit:
        min_digit = un[j]
        
    j+=1
        
print("Here is your the biggest digit: ", max_digit)
print("Here is your the smallest digit: ", min_digit)
