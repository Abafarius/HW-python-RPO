class Animal:
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
        self.alive = True

    def talk(self):
        print("Mmmmmmm...")

    def eat(self, meal):
        self.size += len(meal)
        self.weight += len(meal)