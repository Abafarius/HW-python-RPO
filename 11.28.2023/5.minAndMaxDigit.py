un = input("Enter number: ")

max_digit = "0"
min_digit = "9"


j = 0
for i in un:

    if un[j] >= max_digit:

        max_digit = un[j]

        
    if un[j] <= min_digit:
        min_digit = un[j]
        
    j+=1
        
print("Here is your the biggest digit: ", max_digit)
print("Here is your the smallest digit: ", min_digit)
