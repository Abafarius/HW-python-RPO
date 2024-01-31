class Stars:
    def __init__(self, name, type, distance_ly, mass_kg, radius_km, temperature_kelvin, luminosity, age_years, composition, constellation):
        self.name = name
        self.type = type
        self.distance_ly = distance_ly
        self.mass_kg = mass_kg
        self.radius_km = radius_km
        self.temperature_kelvin = temperature_kelvin
        self.luminosity = luminosity
        self.age_years = age_years
        self.composition = composition
        self.constellation = constellation

    def get_surface_gravity(self):
        # Calculate surface gravity using Newton's law of universal gravitation
        G = 6.67430e-11  # gravitational constant
        return (G * self.mass_kg) / (self.radius_km ** 2)

    def is_main_sequence(self):
        # Check if the star is in the main sequence phase
        if self.type.lower() == "main sequence":
            return True
        else:
            return False

    def get_temperature_celsius(self):
        # Convert temperature from Kelvin to Celsius
        return self.temperature_kelvin - 273.15

# Пример использования класса Stars
# Создание экземпляра звезды
sun = Stars("Sun", "Main Sequence", 0, 1.989e30, 695700, 5778, 3.828e26, 4.6e9, "Hydrogen, Helium", "Not Applicable")

# Вывод информации о звезде
print("Информация о звезде:")
print("Имя:", sun.name)
print("Тип:", sun.type)
print("Расстояние до Земли (в световых годах):", sun.distance_ly)
print("Масса (в кг):", sun.mass_kg)
print("Радиус (в км):", sun.radius_km)
print("Температура (в Кельвинах):", sun.temperature_kelvin)
print("Светимость:", sun.luminosity)
print("Возраст (в лет):", sun.age_years)
print("Состав:", sun.composition)
print("Созвездие:", sun.constellation)

# Вызов методов для демонстрации их работы
print("Гравитация на поверхности звезды (в м/с^2):", sun.get_surface_gravity())
print("Звезда находится на главной последовательности?", sun.is_main_sequence())
print("Температура звезды (в градусах Цельсия):", sun.get_temperature_celsius())