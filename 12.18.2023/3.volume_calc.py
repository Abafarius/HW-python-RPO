Pi = 3.14
def volume_calc(diameter, height):
    if type(diameter) in (int,float) or type(height) in (int,float):
        Volume = Pi*(diameter**2)*height
        print("The volume of a thing: ", Volume)
        return Volume
    else:
        print("Args must be integer or float numbers!")

data1 = input("Enter an integer or float number for diameter: ")
try:
    value1 = float(data1)
except ValueError:
    print("It's not an integer or float number!")
    exit()

data2 = input("Enter an integer or float number for height: ")
try:
    value2 = float(data2)
except ValueError:
    print("It's not an integer or float number!")
    exit()


try:
    volume_calc(value1, value2)
except TypeError:
    print("Function must have just 2 args")
    exit()
except NameError:
    print("Args have to be an integer numbers")
    exit()

