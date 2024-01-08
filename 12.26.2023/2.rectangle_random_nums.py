import random

def create_random_matrix(rows, columns):
    matrix = [[random.randint(-20, 20) for _ in range(columns)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        row_str = " ".join(str(cell) for cell in row)
        print(row_str)

data1 = input("Enter the number of rows: ")
data2 =  input("Enter the number of columns: ")
try:
    rows = int(data1)
    columns = int(data2)
except ValueError:
    print("Error: Enter integers for the number of rows and columns.")
    exit()

matrix = create_random_matrix(rows, columns)
print("Your matrix:")
print_matrix(matrix)



