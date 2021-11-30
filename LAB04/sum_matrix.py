import random

def create_matrix(matrix_size):
    new_matrix = []
    if len(matrix_size) == 2:
        for i in range(matrix_size[0]):
            new_matrix.append([0]*matrix_size[1])
        return new_matrix
    else:
        raise ValueError("Matirx size is not two dimension")

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

def check_dimension(matrix1, matrix2):
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        return True
    else:
        return False

def show_matrix(matrix):
    for _ in matrix:
        print(f"{_}\n")

def add_matrix(matrix1, matrix2):
    if check_dimension(matrix1, matrix2):
        row = len(matrix1)
        col = len(matrix1[0])
        sum_matrix = create_matrix((row, col))

        for j in range(row):
            for k in range(col):
                sum_matrix[j][k] = matrix1[j][k] + matrix2[j][k]
        return sum_matrix
    else:
        raise ValueError("Matrix dimension is not the same")

if __name__ == '__main__':
    matrix1 = create_random_matrix((128,128))
    matrix2 = create_random_matrix((128,128))
    sum_matrix = add_matrix(matrix1, matrix2)
    #print(sum_matrix)
    #show_matrix(sum_matrix)
    