#Asking for day and night temp-s from user
day_temp_user = input("Enter day temp:")
night_temp_user = input("Enter night temp:")


try:
    #Translating string to int
    day_temp = int(day_temp_user)
    night_temp = int(night_temp_user)
except ValueError: 
    print("Enter valid number")
else:
    #Calculating temperature difference between day and night
    disperse_temp = abs(day_temp-night_temp)
    #print result
    print("Here is difference between day and night temperature:", disperse_temp)


