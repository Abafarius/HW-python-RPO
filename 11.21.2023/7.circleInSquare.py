import math
user_rad = input("Enter the radius of the circle: ")
user_side_length = input("Enter the side of the square: ")

try:
    radius = float(user_rad)
    side_length = float(user_side_length)

except ValueError:

    print("Пожалуйста, введите корректные числовые значения.")
else:
    circle_area = math.pi * radius**2
    square_area = side_length**2

    if circle_area <= square_area:
        print("The circle can fit within the specified square.")
    else:
        print("The circle can't fit within the specified square.")