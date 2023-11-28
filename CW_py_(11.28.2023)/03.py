user_data = input("Enter a word: ")
#user_length = len(user_data)
# for word_num in range(2,user_length,3):
#     print(user_data[word_num])
position = 1
for char in user_data:
    if position%3 == 0:
        print(char)
    position+=1