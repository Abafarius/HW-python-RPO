source = [-7, 3, 76, 0, -65, 7, -7, 3]
result = []
for i in source:
    if i < 0:
        result.append(-1)
    elif i > 0:
        result.append(1)
    else:
        result.append(0)
print(result)