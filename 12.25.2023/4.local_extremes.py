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

#VN: хорошая работа, но для реального использования такая функция не годится. Функция - это инструмент,
# который должен быть как можно более узкоспециализирован, а не делал всю задачу целиком.
# Поясню: лучше всего было бы сделать функцию по такому тесту: 
# find_extremes([15, 20, 16, 25, 18, 22, 20]) == {'max': ((2,20), (4,25), (6,22)), 'min': ((3,16), (5,18))}
# а для форматирования результата сделать другую функцию которая будет работать так:
# extremes_to_str({'max': ((2,20), (4,25), (6,22)), 'min': ((3,16), (5,18))}) == "Maxima: day 2 - 20°C, day 4 - 25°C, day 6 - 22°C", "Minima: day 3 - 16°C, day 5 - 18°C"
# Такое решение будет более практическим.

# Кстати, вы не решили задачи!))) Вы написали только необходимые функции, а в заданиях есть 
# ещё и взаимодействие с пользователем и вывод и тд.))