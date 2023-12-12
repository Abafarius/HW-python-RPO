filename = 'input.txt'
try:
    my_file = open(filename)
except FileNotFoundError:
    print("File not Found")
    exit()

text = my_file.read
my_file.close()
print(text)
