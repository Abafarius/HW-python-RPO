input_str = input("Введите сообщение: ")
key = 1
output_str = ""

alphabet_ru = "абвгдеёжзиклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮ"

for letter in input_str:
    if letter in alphabet_ru:
        ix = alphabet_ru.index(letter)
        new_ix = ix + key
        if new_ix >= len(alphabet_ru):
            new_ix -= len(alphabet_ru)
        output_str += alphabet_ru[new_ix]
    else:
        output_str += letter

print(output_str)