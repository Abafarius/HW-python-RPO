Palindrome = input("Enter a word with 5 letters:")

#"isalpha" method checks is there any kind of alphabetical letter. If it's not returns false. If there will be numbers it will give false
if len(Palindrome) == 5 and Palindrome.isalpha():

    letter1 = Palindrome[0]
    letter2 = Palindrome[1]
    letter3 = Palindrome[2]
    letter4 = Palindrome[3]
    letter5 = Palindrome[4]


    if letter1 == letter5 and letter2 == letter4:
        print("The word", Palindrome, "is Palindrome.")
    else:
        print("The word", Palindrome, "is not Palindrome.")
else:
    print("Please enter a valid five letter word.")


