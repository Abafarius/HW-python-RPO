def find_extremes(temperatures):
    maxima = []
    minima = []

    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            maxima.append((i + 1, temperatures[i]))
        elif temperatures[i - 1] > temperatures[i] < temperatures[i + 1]:
            minima.append((i + 1, temperatures[i]))

    return {'max': tuple(maxima), 'min': tuple(minima)}

def extremes_to_str(extremes):
    maxima_str = "Maxima: " + (", ".join([f"day {day} - {temp}°C" for day, temp in extremes['max']]) if extremes['max'] else "")
    minima_str = "Minima: " + (", ".join([f"day {day} - {temp}°C" for day, temp in extremes['min']]) if extremes['min'] else "")

    return maxima_str, minima_str

def test_find_extremes():
    assert find_extremes([15, 20, 16, 25, 18, 22, 20]) == {'max': ((2, 20), (4, 25), (6, 22)), 'min': ((3, 16), (5, 18))}
    assert find_extremes([10, 12, 8, 15, 13, 11, 14]) == {'max': ((2, 12), (4, 15)), 'min': ((3, 8), (6, 11))}
    assert find_extremes([]) == {'max': (), 'min': ()}
    assert find_extremes([20, 18, 22, 17, 23, 19, 21]) == {'max': ((3, 22), (5, 23)), 'min': ((2, 18), (4, 17), (6, 19))}
    print("done.")

def test_extremes_to_str():
    assert extremes_to_str({'max': ((2, 20), (4, 25), (6, 22)), 'min': ((3, 16), (5, 18))}) == ("Maxima: day 2 - 20°C, day 4 - 25°C, day 6 - 22°C", "Minima: day 3 - 16°C, day 5 - 18°C")
    assert extremes_to_str({'max': ((2, 12), (4, 15)), 'min': ((3, 8), (6, 11))}) == ("Maxima: day 2 - 12°C, day 4 - 15°C", "Minima: day 3 - 8°C, day 6 - 11°C")
    assert extremes_to_str({'max': (), 'min': ()}) == ("Maxima: ", "Minima: ")
    assert extremes_to_str({'max': ((3, 22), (5, 23)), 'min': ((2, 18), (4, 17), (6, 19))}) == ("Maxima: day 3 - 22°C, day 5 - 23°C", "Minima: day 2 - 18°C, day 4 - 17°C, day 6 - 19°C")
    print("done.")

test_find_extremes()
test_extremes_to_str()



data = input("Put the list of integer numbers here, split them by space: ")
row_nums = data.split(" ")
length_list = len(row_nums)
temperatures = []
for i in range(length_list):
    try:
        translate = int(row_nums[i])
        temperatures.append(translate)
    except ValueError:
       print("You got wrong value!")
       exit()

extremes = find_extremes(temperatures)
result = extremes_to_str(extremes)
print(result)
#VN: хорошая работа, но для реального использования такая функция не годится. Функция - это инструмент,
# который должен быть как можно более узкоспециализирован, а не делал всю задачу целиком.
# Поясню: лучше всего было бы сделать функцию по такому тесту: 
# find_extremes([15, 20, 16, 25, 18, 22, 20]) == {'max': ((2,20), (4,25), (6,22)), 'min': ((3,16), (5,18))}
# а для форматирования результата сделать другую функцию которая будет работать так:
# extremes_to_str({'max': ((2,20), (4,25), (6,22)), 'min': ((3,16), (5,18))}) == "Maxima: day 2 - 20°C, day 4 - 25°C, day 6 - 22°C", "Minima: day 3 - 16°C, day 5 - 18°C"
# Такое решение будет более практическим.

# Кстати, вы не решили задачи!))) Вы написали только необходимые функции, а в заданиях есть 
# ещё и взаимодействие с пользователем и вывод и тд.))