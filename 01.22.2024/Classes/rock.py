class Rock:
    def __init__(self, name, weight_kg, hardness, color):
        self.name = name
        self.weight_kg = weight_kg
        self.hardness = hardness
        self.color = color

    def get_info(self):
        info = f"Название: {self.name}\nВес: {self.weight_kg} кг\nТвердость: {self.hardness}\nЦвет: {self.color}"
        return info

    def smash(self):
        print(f"{self.name} разбил что-то.")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Цвет камня {self.name} изменен на {new_color}.")

# Пример использования класса Rock
# Создание экземпляра камня
stone = Rock("Гранит", 100, "высокая", "серый")

# Вывод информации о камне
print(stone.get_info())

# Изменение цвета камня
stone.change_color("черный")

# Повторный вывод информации о камне
print(stone.get_info())