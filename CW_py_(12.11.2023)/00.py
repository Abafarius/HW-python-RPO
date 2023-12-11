lyrics = """
i don't wanna close my eyEE
i don't wanna FALL asleep
cause i miss you baby
and i don't want to miss a thing
"""
result = ""
lines = lyrics.split('\n')
for line in lines:
    if line:
        pre_result = line.capitalize().center(36, '-')
        result += pre_result + '\n'
print(result)


