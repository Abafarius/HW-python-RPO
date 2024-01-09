#Замена слова. Разработайте программу, которая заменяет все вхождения заданного слова в тексте на другое слово. Текст читается из файла из файла. Пользователь должен ввести исходное слово и слово, на которое нужно заменить. Программа должна заменить все вхождения исходного слова на новое слово, сохраняя регистр, и вывести текст на экран
#программа -> код
#ПРОГРАММА -> КОД
#Программа -> Код
filename = 'article.txt'
try:
    file = open(filename, encoding='utf-8')
except FileNotFoundError:
    print("File not Found")
    exit()

text = file.read()
file.close()
print(text)
user_input_old = input("Enter a word to replace: ")
user_input_new = input("Enter a new word to replace: ")
user_old_lower = user_input_old.lower()
user_new_lower = user_input_new.lower()
result0 = text.replace(user_old_lower, user_new_lower)
user_input_old.capitalize()
user_input_old.upper()

result = text.replace(user_input_old, user_input_new)
print(result)


