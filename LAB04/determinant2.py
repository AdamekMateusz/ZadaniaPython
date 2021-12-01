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

def swap(matrix, counter):
    copy = matrix
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        for u in range(col):
            if u == row -1:
                copy[0] = matrix[u]
            else:
                copy[u+1] = matrix[u]
    return copy

def determinat(matrix):
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

def determinat(matrix):
    matrix_copy = matrix
    row = len(matrix)
    col = len(matrix[0])

    p_operator = [1]

    for i in range(row):
        for j in range(row):
            if i >= j:
                continue
            wspol = matrix[j][i]/matrix[i][i]
            for k in range(col):
                matrix[j][k] = matrix[j][k] - matrix[i][k]*wspol
                #matrix[k][j] = (matrix_copy[i][i] * matrix_copy[k][j] - matrix_copy[k][i] * matrix_copy[i][j])/p_operator[i]
            print(wspol)
    show_matrix(matrix)
    

    # for i in range(row):
    #     for j in range(row):
    #         if i >= j:
    #             continue
    #         wspol = matrix[j][0]/matrix[i][i]
    #         for k in range(col):
    #             matrix[j][k] = matrix[j][k] - matrix[i][k]*wspol
    #             #matrix[k][j] = (matrix_copy[i][i] * matrix_copy[k][j] - matrix_copy[k][i] * matrix_copy[i][j])/p_operator[i]
    #         print(wspol)
    # show_matrix(matrix)
    det = 1
    for m in range(row):
        for n in range(col):
            if m == n:
                det *= matrix[m][n]
    print("det ", det)
                


if __name__ == '__main__':
    matrix1 = [
        [25,5,1],
        [64,8,1],
        [144,12,1]
    ]
    determinat(matrix1)
    #print(determinat(matrix1))
        