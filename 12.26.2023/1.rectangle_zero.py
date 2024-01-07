import random

def create_random_matrix(rows, columns):
#VN: тут была лишняя пустая строка
    matrix = [[random.randint(-20, 20) for _ in range(columns)] for _ in range(rows)]
    return matrix

def print_matrix(matrix):
#VN: тут была лишняя пустая строка
    for row in matrix:
        row_str = " ".join(str(cell) for cell in row)
        print(row_str)

def main():
#VN: тут была лишняя пустая строка
    try:
        #VN: тут была лишняя пустая строка
        rows = int(input("Enter the number of rows: "))
        columns = int(input("Enter the number of columns: "))

        #VN: тут была лишняя пустая строка
        #VN: все последующие строки в блоке try лишние!
        matrix = create_random_matrix(rows, columns)


        print("Your matrix:")
        print_matrix(matrix)

    except ValueError:
        print("Error: Enter integers for the number of rows and columns.")

if __name__ == "__main__":
    main()
