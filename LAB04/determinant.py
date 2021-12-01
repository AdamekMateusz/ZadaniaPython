import random

def create_random_matrix(matrix_size):
    if len(matrix_size) != 2:
        raise ValueError("Wrong matrix size")
    matrix = []
    for i in range(matrix_size[0]):
        row = []
        for j in range(matrix_size[1]):
            row.append(random.randint(0,100))
        matrix.append(row)
    return matrix

def refresh(matrix_copy, matrix):
    matrix_copy = matrix
    return matrix_copy

def determinat_checker(matrix):
    check = []
    for j in range(len(matrix)):
        for k in range(len(matrix[0])):
            if matrix[j][j] != 0:
                check.append(matrix[j][j])
            if matrix[j][k] != 0:
                return 0
    
    if all(element == check[0] for element in check):
        return 1
            
def show_matrix(matrix):
    for _ in matrix:
        print(f"{_}\n")

def diagonal(matrix):
    matrix_copy = matrix
    row = len(matrix)
    col = len(matrix[0])

    p_operator = [1]

    for i in range(row):
        for j in range(row):
            if i == j:
                continue
            for k in range(col):
                print('************')
                print("MATRIX[k][j]",matrix[k][j])
                print('operation',(matrix_copy[i][i] * matrix_copy[k][j] - matrix_copy[k][i] * matrix_copy[i][j])/p_operator[i])
                print(matrix_copy[i][i])
                print(matrix_copy[k][j])
                print(matrix_copy[k][i])
                print(matrix_copy[i][j])
                print('*****************')
                matrix[k][j] = (matrix_copy[i][i] * matrix_copy[k][j] - matrix_copy[k][i] * matrix_copy[i][j])/p_operator[i]
            print('AFTTER', matrix[k][j])
            print('Do show')
            show_matrix(matrix)

        #matrix_copy = matrix
        matrix_copy = refresh(matrix_copy, matrix) 
        p_operator.append(matrix[i][i])
    
    matrix_copy = refresh(matrix_copy, matrix)

    show_matrix(matrix_copy)

    if determinat_checker(matrix_copy):
        return matrix[0][0]
    else:
        print('Mathematical error')
        return None

if __name__ == '__main__':
    matrix1 = [
        [5,3,2],
        [5,2,12],
        [4,2,9]
    ]

    print(diagonal(matrix1))
        