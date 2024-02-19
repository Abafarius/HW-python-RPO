from goose import Goose
from wolf import Wolf

# Создаем экземпляры классов
goose1 = Goose("White Goose", 5, 30, ["grass", "corn"], "white")
goose2 = Goose("Grey Goose", 6, 32, ["grass", "wheat"], "grey")
wolf1 = Wolf("Big Bad Wolf", 40, 70, "grey")
wolf2 = Wolf("Alpha Wolf", 45, 75, "black")

# Поиграем с животными
goose1.talk()  # Ожидаемый вывод: "Honk! Honk!"
wolf1.talk()   # Ожидаемый вывод: "Awooooo!"

wolf1.eat(goose1)  # Ожидаемый вывод: "Big Bad Wolf can't eat White Goose."
wolf1.eat(wolf2)   # Ожидаемый вывод: "Big Bad Wolf can't eat Alpha Wolf."

wolf1.eat(goose2)  # Ожидаемый вывод: "Awooooo!"
print(f"Wolf's weight after eating: {wolf1.weight}")  # Ожидаемый вывод: Wolf's weight after eating: 46.0
print(f"Wolf's size after eating: {wolf1.size}")  