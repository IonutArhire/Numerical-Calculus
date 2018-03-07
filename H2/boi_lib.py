import numpy as np
import math


def search_pivot(matrix, n, l):
    ''' Partial pivoting version '''
    candidates = np.squeeze(matrix[l:n, l:(l+1)])
    return np.absolute(candidates).argmax() + l


def adjust_pivot(matrix, l, idx_pivot):
    ''' Partial pivoting version '''
    matrix[[l, idx_pivot]] = matrix[[idx_pivot, l]]


def eliminate(matrix, n, l):
    curr_row = l + 1
    while curr_row != n:
        modified_pivot = matrix[l] * (matrix[curr_row, l] / matrix[l, l])
        matrix[curr_row] -= modified_pivot
        curr_row += 1


def solve_system(matrix, n):
    solution = []
    row = n - 1
    while row >= 0:
        new_unknown = matrix[row, n] - (matrix[row:row + 1, row + 1:n] * solution).sum()
        new_unknown /= matrix[row, row]

        solution = [new_unknown] + solution

        row -= 1
    return np.asarray(solution).reshape(len(solution), 1)


def extract_coefficient_matrix(augmented_matrix, n):
    return augmented_matrix[0:n, 0:n]


def extract_free_terms(augmented_matrix, n):
    return augmented_matrix[0:n, n:n+1]


def verify_solution(matrix, n, solution, p):
    coefficients = extract_coefficient_matrix(matrix, n)
    free_terms = extract_free_terms(matrix, n)

    result = np.linalg.norm(coefficients.dot(solution) - free_terms, ord=2)

    return result < 10 ** -p


def get_inverse(matrix):
    return np.linalg.inv(matrix)


def gauss_elimination(initial_matrix, n, e):
    matrix = initial_matrix.copy()
    p = 4 + math.log10(float(n))
    l = 0
    solution = []

    while l < n - 1 and abs(matrix[l, l]) > e:
        idx_pivot = search_pivot(matrix, n, l)
        if idx_pivot != l:
            adjust_pivot(matrix, l, idx_pivot)
            print(f"Step {l}:\n", matrix, "\n")
        eliminate(matrix, n, l)
        print(f"Step {l}:\n", matrix, "\n")
        l += 1
    if abs(matrix[l, l]) <= e:
        raise Exception('Singular matrix!\n')
    else:
        solution = solve_system(matrix, n)
        print("Solution:\n", solution, "\n")
        print("Is solution valid: ", verify_solution(
            initial_matrix, n, solution, p), "\n")
    return solution
