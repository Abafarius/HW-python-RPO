from functools import reduce
numbers = [5,6,-8,33,5]
result = map(lambda x: -x, numbers)
#print(result)

even = filter(lambda x: x%2 == 0, result)
#print(even)

multi = reduce(lambda acc, x: acc * x, even)
print(multi)