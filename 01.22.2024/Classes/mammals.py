class Mammals:
    gender = 0
    weight = 0
    size = 0
    age = 0
    type_food_eater = ""


    def __init__(self, age):
        self.age = age
        return self.age
    
    def get_type_food_eater(self, food_eater):
        self.type_food_eater = food_eater
        return Mammals()


cat = Mammals(2)
predator = cat.get_type_food_eater("predator")
    
        