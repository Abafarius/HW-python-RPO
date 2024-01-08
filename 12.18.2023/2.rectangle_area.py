def get_rectanlge_area(length, width = None):
    if not width is None:
        area = length*width
        return area
    square_area = length**2
    return square_area

data1 = input("Enter an integer number for length: ")
try:
    value1 = int(data1)
except ValueError:
    print("It's not an integer number!")
    exit()

data2 = input("Enter an integer number for width: ")
if data2 == "":
    value2 = None
else:
    try:
        value2 = int(data2)
    except ValueError:
        print("It's not an integer number!")
        exit()

if value2 == None:
    square_area =  get_rectanlge_area(value1, value2)
    print("The area of square: ", square_area)
else:
    area = get_rectanlge_area(value1, value2)
    print("The area of rectangle: ", area)
