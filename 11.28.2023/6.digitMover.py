# Запросить у пользователя число
number = input("Введите число: ")

# Проверка на корректность ввода числа
if not number.isdigit():
    print("Пожалуйста, введите корректное число.")
else:
    # Запросить на сколько цифр сдвинуть число
    shift = int(input("На сколько цифр сдвинуть число: "))

    # Преобразовать строку в список цифр
    digits = [int(digit) for digit in number]

    # Выполнить сдвиг цифр
    shifted_digits = digits[shift:] + digits[:shift]

    # Преобразовать список цифр обратно в строку
    result = ''.join(map(str, shifted_digits))

    # Вывести результат
    print("Результат сдвига:", result)