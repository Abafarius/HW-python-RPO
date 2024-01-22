class Person:
    name = "No name"
    age = 0
    weight = 3.500
    gender = "none"
    colour = "transparent"
    country = "Kazakhstan"


    def __init__(self, gender, name, color):
        self.name = name
        self.gender = gender
        self.colour = color
        
    def grow(self, years):
        self.age += years
        self.weight += years * 2


man = Person('male', "Sanya Kozhegambetov", 'pink')
man.grow(3)
print(man.name, man.age, man.weight)
man.grow(3)
print(man.name, man.age, man.weight)