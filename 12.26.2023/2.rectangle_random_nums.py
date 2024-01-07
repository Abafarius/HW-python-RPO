import random

def create_random_matrix(rows, columns):

    matrix = [[random.randint(-20, 20) for _ in range(columns)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):

    for row in matrix:
        row_str = " ".join(str(cell) for cell in row)
        print(row_str)

def main():

    try:

        rows = int(input("Введите количество строк: "))
        columns = int(input("Введите количество столбцов: "))


        matrix = create_random_matrix(rows, columns)


        print("Ваша матрица:")
        print_matrix(matrix)

    except ValueError:
        print("Error: Enter integers for the number of rows and columns.")

if __name__ == "__main__":
    main()