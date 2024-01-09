user_word = input("Enter a word (if you  want remove a letter put '@' after this letter): ")
letters = list(user_word)
length_word = len(user_word)
for i in letters:
    if i == "@":
        index_target = letters.index("@") - 1
        removed = letters.pop(index_target)
        removed2 = letters.remove(i)
word = "".join(letters)
print(word)

