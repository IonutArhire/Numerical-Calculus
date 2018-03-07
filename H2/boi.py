from boi_lib import *


def get_input_params():
    with open("input_params.txt") as f:
        fst_line = f.readline().split()
        n, e = int(fst_line[0]), float(fst_line[1])
        matrix = np.loadtxt(f)
        return (n, e, matrix)


n, e, matrix = get_input_params()

X = gauss_elimination(matrix, n, e)

A = extract_coefficient_matrix(matrix, n)

A_inv = get_inverse(A)
print("Inverse of A is:\n", A_inv, "\n")

B = extract_free_terms(matrix, n)

X_lib = np.linalg.solve(A, B)

norm1 = np.linalg.norm(X - X_lib, ord=2)
print("||Xgauss - Xlib||2 : ", norm1)

norm2 = np.linalg.norm(X - A_inv.dot(B), ord=2)
print("||Xgauss - A(inv)B||2 : ", norm2)
