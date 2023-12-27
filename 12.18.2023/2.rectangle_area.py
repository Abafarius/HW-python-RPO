def get_rectanlge_area(length, width = None):
    if type(length) is int or type(width) is int:
        if not width is None:
            area = length*width
            print("The area of rectangle: ", area)
            return area
        square_area = length**2
        print("The area of square: ", square_area)
        return square_area
    else:
        print("Args must be integer numbers!")


data1 = input("Enter an integer number for length: ")
try:
    value1 = int(data1)
except ValueError:
    print("It's not an integer number!")
    exit()

data2 = input("Enter an integer number for width: ")
try:
    value2 = int(data2)
except ValueError:
    print("It's not an integer number!")
    exit()


try:
    get_rectanlge_area(value1, value2)
except TypeError:
    print("Function must have just 2 args")
    exit()
except NameError:
    print("Args have to be an integer numbers")
    exit()