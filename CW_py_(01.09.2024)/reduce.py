from functools import reduce
array = (5, 7, 8, 3)

result = reduce(lambda acc, x: acc + x, array)
print(result)


text = "Государственное муниципальное унитарное предприятие ромашка - ассоциация пчеловодов Казахстана"

abbr = reduce(lambda acc, x: acc + x[0].upper(), text.split(" "), "")
print(abbr)