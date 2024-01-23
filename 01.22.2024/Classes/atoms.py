class Atoms:
    radius = 0
    mass = 0
    charge = 0 #True is positive and False is negative charge also 0 is neutral
    crystal_structure =  "None"
    atomic_number = 0


    def __init__(self, atomic_number):
        self.atomic_number = atomic_number

    def charge_change(self, charge):
        self.charge = charge
        return self.charge
    
    def collide(self, another_self):
        self.atomic_number += another_self.atomic_number
        return Atoms(self.atomic_number)


hydrogen1 = Atoms(1)
hydrogen2 = Atoms(1)
hellium = hydrogen1.collide(hydrogen2)
num = hellium.atomic_number
current_charge = hydrogen1.charge_change(True)
print(num)


