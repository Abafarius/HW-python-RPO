def find_local_extremes(temperatures):
    maxima = []
    minima = []

    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            maxima.append(f"day {i + 1} - {temperatures[i]}°C")
        elif temperatures[i - 1] > temperatures[i] < temperatures[i + 1]:
            minima.append(f"day {i + 1} - {temperatures[i]}°C")

    maxima_str = "Maxima: " + (", ".join(maxima) if maxima else "")
    minima_str = "Minima: " + (", ".join(minima) if minima else "")

    return maxima_str, minima_str

def test_find_local_extremes():
    assert find_local_extremes([15, 20, 16, 25, 18, 22, 20]) == ("Maxima: day 2 - 20°C, day 4 - 25°C, day 6 - 22°C", "Minima: day 3 - 16°C, day 5 - 18°C")
    assert find_local_extremes([10, 12, 8, 15, 13, 11, 14]) == ("Maxima: day 2 - 12°C, day 4 - 15°C", "Minima: day 3 - 8°C, day 6 - 11°C")
    assert find_local_extremes([]) == ("Maxima: ", "Minima: ")
    assert find_local_extremes([20, 18, 22, 17, 23, 19, 21]) == ("Maxima: day 3 - 22°C, day 5 - 23°C", "Minima: day 2 - 18°C, day 4 - 17°C, day 6 - 19°C")
    print("done.")
test_find_local_extremes()