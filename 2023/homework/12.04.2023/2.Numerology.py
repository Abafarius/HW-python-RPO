user_word = input("Enter any word: ")
sum = 0
for i in user_word:
    print("Character: ", i)
    num_char = ord(i)
    print("number of character: ", num_char)
    sum += num_char
print("Sum of characters' numbers: ", sum)