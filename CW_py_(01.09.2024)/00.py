array = ['Timur', 'Argyn', 'Sergey', 'Almat', 'Slava', 'Alexander', 'Galym', 'Vitaliy']
new_array = sorted(array, key = lambda a,: len(a))
print(new_array)

#Predicate  это функция-предикат или функция-вопрос. Предикат отвечает на утвердительный вопрос «да» или «нет», возвращая значение типа bool.

#1. map
#2. filter
#3. reduce

result = list(map(lambda x: x[-1], array))
print(result)

user_list = ["2", "4", "45"]
numbers = list(map(int, user_list))
print(numbers)