#Asking for day and night temp-s from user
day_temp = int(input("Enter day temp:"))
night_temp = int(input("Enter night temp:"))

#Calculating temperature difference between day and night
disperse_temp = abs(day_temp-night_temp)

#print result
print("Here is difference between day and night temperature:", disperse_temp)
