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

def show_matrix(matrix):
    for _ in matrix:
        print(f"{_}\n")

def transpose(matrix):
    row_size = len(matrix)
    col_size = len(matrix[0])

    new_matrix = []
    for _ in range(col_size):
        new_matrix.append([0]*row_size)


    for row in range(row_size):
        for col in range(col_size):
            new_matrix[col][row] = matrix[row][col]

    return new_matrix



def multiplu_matrix(matrix1, matrix2):
    matrix2 = transpose(matrix2)
    if len(matrix1) != len(matrix2[0]):
        raise ValueError('Matrix size is incorrect, cannot muliply this matrix')
    new_col = len(matrix1[0])
    new_row = len(matrix2)
    
    new_matrix = []
    for i in range(new_row):
        new_matrix.append([0]*new_col)


    for row in range(len(matrix1)):
        for col in range(len(matrix1[0])):
            sum = 0
            for i in range(len(matrix1)):
                sum = sum + (matrix1[row][i] * matrix2[col][i])
            new_matrix[row][col] = sum

    return new_matrix
    


if __name__ == '__main__':
    matrix_1 = create_random_matrix((8, 8))
    matrix_2 = create_random_matrix((8, 8))

    show_matrix(matrix_1)
    print("**************")
    show_matrix(matrix_2)
    print("**************")
    show_matrix(multiplu_matrix(matrix_1, matrix_2))


