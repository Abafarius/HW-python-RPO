from predator import Predator

class Wolf(Predator):
    def __init__(self, name, weight, size, fur_color):
        super().__init__(name, weight, size)
        self.fur_color = fur_color

    def howl(self):
        print("Awooooo!")

    def talk(self):
        print("Aw! Aw!")
