user_word = input("Enter ANY word: ")
word_length = len(user_word)
prelast_letter = len(user_word)-2
first_letters = user_word[0:2]
last_letters = user_word[prelast_letter:word_length]
shorted = first_letters+"-"+last_letters
print("Here is short version of this word: ", shorted)


