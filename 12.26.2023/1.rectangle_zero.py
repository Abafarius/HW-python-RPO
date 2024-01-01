def create_matrix(rows, columns):
    matrix = [[0] * columns for _ in range(rows)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        row_str = " ".join(str(cell) for cell in row)
        print(row_str)

def main():
    data1 = input("Enter count of rows: ")
    data2 = input("Enter count of columns: ")
    try:
        rows = int(data1)
        columns = int(data2)

        matrix = create_matrix(rows, columns)

        print("Your matrix:")
        print_matrix(matrix)

    except ValueError:
        print("Ошибка: Введите целые числа для количества строк и столбцов.")

if __name__ == "__main__":
    main()
