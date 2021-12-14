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
            
def show_matrix(matrix):
    for _ in matrix:
        print(f"{_}\n")

def determinat(matrix):
    matrix_copy = matrix
    row = len(matrix)
    col = len(matrix[0])
    #check thant all element in row is 0, if is return det=0
    for r in matrix:
        if all(v == 0 for v in r):
            return 0
    col_value = []
    for r in range(row):
        for c in range(col):
            col_value.append(matrix[c][r])
        if all(v == 0 for v in col_value):
            return 0
        else:
            col_value.clear()

    #check if all element in column is equal =0 , if is det=0 
    swap_times = 0

    for i in range(row):
        for j in range(row):
            #to moze byc petla nieskonczona, trzeba tego uniknac
            if matrix[i][i] == 0:
                matrix.append(matrix[j])
                matrix.pop(j)
                swap_times += 1
            if i >= j:
                continue
            wspol = matrix[j][i]/matrix[i][i]
            for k in range(col):
                matrix[j][k] = matrix[j][k] - matrix[i][k]*wspol
    
    det = 1
    for m in range(row):
        for n in range(col):
            if m == n:
                det *= matrix[m][n]
    return ((-1)**swap_times) * det


if __name__ == '__main__':
    # matrix1 = [
    #     [25,5,1],
    #     [64,8,1],
    #     [144,12,1]
    # ]

    # matrix1 = [
    #     [0,0,0],
    #     [64,8,1],
    #     [144,12,1]]

    # matrix1 = [
    #     [0,1,0],
    #     [1,2,0],
    #     [0,3,0]]

    matrix1 = [
        [0,1,3,4],
        [1,2,5,3],    
        [5,7,1,2],    
        [9,3,2,1]]

    print(determinat(matrix1))
    #print(determinat(matrix1))
       