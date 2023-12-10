list_num = [3, 9, 8, 4, 5, 1]
maxi = max(list_num)
mini = min(list_num)
place_max = list_num.index(maxi)
place_mini = list_num.index(mini)
distance = abs(place_max - place_mini)
print("The distance between max and min values of the array: ", distance)