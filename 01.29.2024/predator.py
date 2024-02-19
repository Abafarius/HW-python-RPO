from animal import Animal

class Predator(Animal):
    def __init__(self, name, weight, size):
        super().__init__(name, weight, size)

    def eat(self, prey):
        if isinstance(prey, Animal) and prey.alive and prey.size < self.size and prey.weight < self.weight:
            super().eat("prey")
            self.size += prey.size * 0.2
            self.weight += prey.weight * 0.2
            prey.alive = False
        else:
            print(f"{self.name} can't eat {prey.name}.")