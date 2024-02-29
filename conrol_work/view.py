class AbcView:
    def show(self, text):
        print(text)

    def show_word(self, word):
        print(f"Слово оппонента: {word}")

    def show_win(self):
        print("Поздравляем! Вы выиграли!")

    def show_loose(self):
        print("К сожалению, вы проиграли.")

    def show_mistake(self, last_letter, attempts_left):
        print(f"Неправильный ход. Слово должно начинаться на букву '{last_letter}'.")
        print(f"Осталось попыток: {attempts_left}")

    def show_duplicate(self, attempts_left):
        print("Такое слово уже было использовано.")
        print(f"Осталось попыток: {attempts_left}")

    def show_unknown(self):
        print("Такого слова не существует.")

    def ask_word(self):
        word = input("Введите ваше слово: ")
        while not word or len(word.split()) != 1:
            word = input("Введите одно слово: ")
        return word