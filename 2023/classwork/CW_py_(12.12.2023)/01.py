filename = 'input.txt'
try:
    my_file = open(filename, encoding='utf-8')
except FileNotFoundError:
    print("File not Found")
    exit()

text = my_file.read()
my_file.close()
print(text)
