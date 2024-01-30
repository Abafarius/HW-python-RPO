sun_mass = 1.989*10**30

class Stars:
    spectral_type_of_star = ""
    fuel = 0
    age = 0
    energy = 0
    brightness = 0
    mass = 0
    surface_temp = 0
    radius = 0
    speed = 0
    wave_length = 0
    b_const = 2.897771955*10**(-3) #Wien's displacement constant
    health = 100
    def __init__(self, radius, mass, speed, age, fuel, wave_length):
        self.wave_length = wave_length
        self.radius = radius
        self.mass = mass
        self.speed = speed
        self.age = age
        self.fuel = fuel
        self.energy = (self.mass * self.speed**2)/2
        self.brightness = self.energy*self.radius*self.mass
        self.surface_temp = self.b_const/self.wave_length
        if self.surface_temp >= 30000:
            self.spectral_type_of_star = "O"
        elif self.surface_temp >= 11000 or self.surface_temp < 30000:
            self.spectral_type_of_star = "B"
        elif self.surface_temp > 7200 or self.surface_temp < 11000:
            self.spectral_type_of_star = "A"
        elif self.surface_temp > 6000 or self.surface_temp < 7200:
            self.spectral_type_of_star = "F"
        elif self.surface_temp > 5200 or self.surface_temp < 6000:
            self.spectral_type_of_star = "G"
        elif self.surface_temp > 3500 or self.surface_temp < 5200:
            self.spectral_type_of_star = "K"
        elif self.surface_temp < 3500:
            self.spectral_type_of_star = "M"

    
sun = Stars()