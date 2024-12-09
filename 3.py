def add_matrices(matrix_a, matrix_b): 
    """Returns the sum of two matrices.""" 
    if len(matrix_a) == 0 or len(matrix_b) == 0: 
        return [] 
    rows = len(matrix_a) 
    cols = len(matrix_a[0]) 
    # Check if dimensions match 
    if rows != len(matrix_b) or cols != len(matrix_b[0]): 
        raise ValueError("Matrices must have the same dimensions for addition.") 
    result = [[0 for _ in range(cols)] for _ in range(rows)] 
    for i in range(rows): 
        for j in range(cols): 
            result[i][j] = matrix_a[i][j] + matrix_b[i][j] 
    return result 

def subtract_matrices(matrix_a, matrix_b): 
    """Returns the difference of two matrices.""" 
    if len(matrix_a) == 0 or len(matrix_b) == 0: 
        return [] 
    rows = len(matrix_a) 
    cols = len(matrix_a[0]) 
    # Check if dimensions match 
    if rows != len(matrix_b) or cols != len(matrix_b[0]): 
        raise ValueError("Matrices must have the same dimensions for subtraction.") 
    result = [[0 for _ in range(cols)] for _ in range(rows)] 
    for i in range(rows): 
        for j in range(cols): 
            result[i][j] = matrix_a[i][j] - matrix_b[i][j] 
    return result 

def multiply_matrices(matrix_a, matrix_b): 
    """Returns the product of two matrices.""" 
    if len(matrix_a) == 0 or len(matrix_b) == 0: 
        return [] 
    rows_a = len(matrix_a) 
    cols_a = len(matrix_a[0]) 
    rows_b = len(matrix_b) 
    cols_b = len(matrix_b[0]) 
    # Check if multiplication is possible 
    if cols_a != rows_b: 
        raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix.") 
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)] 
    for i in range(rows_a): 
        for j in range(cols_b): 
            for k in range(cols_a): 
                result[i][j] += matrix_a[i][k] * matrix_b[k][j] 
    return result 

def transpose_matrix(matrix): 
    """Returns the transpose of a matrix.""" 
    if len(matrix) == 0: 
        return [] 
    rows = len(matrix) 
    cols = len(matrix[0]) 
    result = [[0 for _ in range(rows)] for _ in range(cols)] 
    for i in range(rows): 
        for j in range(cols): 
            result[j][i] = matrix[i][j] 
    return result 

# Sample matrices 
matrix_a = [ 
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9] 
] 
matrix_b = [ 
    [9, 8, 7], 
    [6, 5, 4], 
    [3, 2, 1] 
] 

# Function calls 
added_matrix = add_matrices(matrix_a, matrix_b) 
subtracted_matrix = subtract_matrices(matrix_a, matrix_b) 
multiplied_matrix = multiply_matrices(matrix_a, matrix_b) 
transposed_matrix = transpose_matrix(matrix_a) 

# Output results 
print("Matrix A:") 
for row in matrix_a: 
    print(row) 

print("\nMatrix B:") 
for row in matrix_b: 
    print(row) 

print("\nAddition of Matrix A and B:") 
for row in added_matrix: 
    print(row) 

print("\nSubtraction of Matrix A and B:") 
for row in subtracted_matrix: 
    print(row) 

print("\nMultiplication of Matrix A and B:") 
for row in multiplied_matrix: 
    print(row) 

print("\nTranspose of Matrix A:") 
for row in transposed_matrix: 
    print(row)
