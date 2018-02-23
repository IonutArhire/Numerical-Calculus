# Ex. 1

def u():
    u = 1.0
    while 1 + u != 1:
        u /= 10
    return u * 10

print('precision is', u())

# Ex. 2

def ver_add():
    x = 1.0
    y = u()
    z = u()
    return ((x + y) + z) == (x + (y + z))

def ver_mul():
    x = 3
    y = 0.7
    z = 0.3

    # assoc = False
    # Explanation: 
    # (x * y) = 2.099999999
    # ((x * y) * z) = 0.6299999999
    # but 
    # (y * z) = 0.21
    # (x * (y * z)) = 0.63 
    return ((x * y) * z) == (x * (y * z))

print('add asoc?', ver_add())
print('mul asoc?', ver_mul())

# Ex. 3

import numpy as np

def create_sample_matrix(n):
    sample = np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            sample[i,j] = i * n + j
    return sample

def strassen_partition(X, n):
    mid = n//2
    X11 = X[0:mid, 0:mid]
    X12 = X[0:mid, mid:]
    X21 = X[mid:, 0:mid]
    X22 = X[mid:, mid:]

    return (X11, X12, X21, X22)

def strassen_result(C11, C12, C21, C22, n):
    result = np.zeros(shape=(n,n))

    mid = n//2
    result[0:mid, 0:mid] = C11
    result[0:mid, mid:] = C12
    result[mid:, 0:mid] = C21
    result[mid:, mid:] = C22

    return result

def strassen_mul(A, B, n, n_min):
    if n <= n_min:
        return A.dot(B)
    else:
        A11, A12, A21, A22 = strassen_partition(A, n)
        B11, B12, B21, B22 = strassen_partition(B, n)

        P1 = strassen_mul((A11 + A22), (B11 + B22), n//2, n_min)
        P2 = strassen_mul((A21 + A22), B11, n//2, n_min)
        P3 = strassen_mul(A11, (B12 - B22), n//2, n_min)
        P4 = strassen_mul(A22, (B21 - B11), n//2, n_min)
        P5 = strassen_mul((A11 + A12), B22, n//2, n_min)
        P6 = strassen_mul((A21 - A11), (B11 + B12), n//2, n_min)
        P7 = strassen_mul((A12 - A22), (B21 + B22), n//2, n_min)

        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6
        
        return strassen_result(C11, C12, C21, C22, n)

A = create_sample_matrix(4)
B = create_sample_matrix(4)

print(A, '\n')
print(B, '\n')
print(strassen_mul(A, B, 4, 2))