def get_scalar(vector_a, vector_b):
    if len(vector_a) != len(vector_b):
        raise ValueError("Vector is not the same size")
    
    sum = 0
    for i in range(len(vector_a)):
        sum += vector_a[i] * vector_b[i]
    return sum


if __name__ == '__main__':
    vector_A = [1,2,12,4]
    vector_B = [2,4,2,8]

    print(get_scalar(vector_A, vector_B))