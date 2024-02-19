from animal import Animal

class Herbivore(Animal):
    def __init__(self, name, weight, size, diet):
        super().__init__(name, weight, size)
        self.diet = diet

    def eat(self, meal):
        if meal in self.diet:
            super().eat(meal)
        else:
            print(f"{self.name} doesn't eat {meal}.")