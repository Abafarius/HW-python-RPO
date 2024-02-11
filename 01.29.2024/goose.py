from herbivore import Herbivore

class Goose(Herbivore):
    def __init__(self, name, weight, size, diet, color):
        super().__init__(name, weight, size, diet)
        self.color = color

    def honk(self):
        print("Quack! Quack!")

    def talk(self):
        print("Honk! Honk!")