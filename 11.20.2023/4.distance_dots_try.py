#Asking for coordinates from user
user_x1 = input("Enter 1st x dot: ")
user_x2 = input("Enter 2st x dot: ")
user_y1 = input("Enter 1nd y dot: ")
user_y2 = input("Enter 2nd y dot: ")

#Translating user data to integer
try:
    x1 = int(user_x1)
    x2 = int(user_x2)
    y1 = int(user_y1)
    y2 = int(user_y2)
except ValueError:
    print("You didin't enter valid number, so continue the program. Start it again my dear user. You have to enter integer number like '123456789'.")
else:

    #Calculating distance between 2 dots
    distance_dots = ((x1-x2)**2+(y1-y2)**2)**0.5

    #print result
    print("distance between dots: ", distance_dots)
