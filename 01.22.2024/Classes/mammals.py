class Mammals:
    gender = 0
    weight = 0
    height = 0
    age = 0
    type_food_eater = ""
    health = 100


    def __init__(self, age, type_food_eater, gender):
        self.age = age
        self.type_food_eater = type_food_eater
        self.gender = gender
        self.weight += age*1.8
        self.height += self.weight + 100

    def get_grow(self, age):
        self.weight += 5
        self.height += 100+self.weight
        self.age = age 

    def get_feed(self, food_num):
        self.weight += food_num/100

    def get_attack(self, other_self, damage):
        if self.weight > other_self.weight:
            self.health -= damage*0.2
            other_self.health -= damage
        else:
            self.health -= damage
            other_self.health -= damage*0.2            


cat = Mammals(2, "predator", "female")
print(cat.age)
cat.get_grow(10)
print(cat.age, cat.weight, cat.height, cat.gender, cat.type_food_eater)

cat.get_feed(306)
print(cat.weight)

whale = Mammals(150, "everything", "female")
whale.get_attack(cat, 100)
    
print(whale.health, cat.health)        