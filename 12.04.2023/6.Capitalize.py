#Ввод слова
word = input("Enter a word: ")

#Проверить, что введена не пустая строка
if len(word) > 0:
    #Определить код ASCII для буквы 'a' и 'A'
    lowercase_a = ord('a')
    uppercase_a = ord('A')
    lowercase_a_rus = ord("а")
    uppercase_a_rus = ord('А')

    #На английском
    #Преобразовать первую букву слова в верхний регистр (если это буква)
    first_letter_code = ord(word[0])
    if lowercase_a <= first_letter_code <= lowercase_a + 25:
        #Если первая буква - строчная, преобразовать ее в заглавную
        first_letter = chr(first_letter_code - lowercase_a + uppercase_a)
    else:
        #Если первая буква не является строчной буквой, оставить без изменений
        first_letter = word[0]
            #На русском
        if lowercase_a_rus <= first_letter_code <= lowercase_a_rus + 31:
        #Если первая буква - строчная, преобразовать ее в заглавную
            first_letter = chr(first_letter_code - lowercase_a_rus + uppercase_a_rus)
        else:
        #Если первая буква не является строчной буквой, оставить без изменений
            first_letter = word[0]



    #Соединить первую букву с оставшейся частью слова
    result = first_letter + word[1:]

    #Вывести результат
    print("The word with capitalized letter:", result)
else:
    print("No way enter a word not empty space")


"""VN: на русском работает, на английском - нет.

Я бы сделал два простых условия:
if "a" <= first_letter <= "z":
    # преобразование со сдвигом из английского набора символов
elif "а" <= first_letter <= "я":
    # преобразование со сдвигом из русского набора
else:
    # просто копируем исходную строку
"""
#Нужно было условие для русского внести в условие для английского