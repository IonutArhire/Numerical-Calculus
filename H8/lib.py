import numpy as np



# MULLER METHOD

def get_max_coef(poly):
    return abs(max(poly[1:].min(), poly[1:].max(), key=abs))

def get_domain(poly):
    A = get_max_coef(poly)
    a0 = abs(poly[0])
    R = (a0 + A) / a0
    return (-R, R)

def get_initial_values(domain, n):
    return np.random.uniform(domain[0], domain[1], n)

def plug_in_poly(poly, val):
    b = poly[0]
    counter = 1
    while counter < len(poly):
        b = poly[counter] + b * val
        counter = counter + 1

    return b

def compute_h0(three_x):
    return three_x[1] - three_x[0]

def compute_h1(three_x):
    return three_x[2] - three_x[1]

def compute_delta0(poly, three_x):
    return (plug_in_poly(poly, three_x[1]) \
        - plug_in_poly(poly, three_x[0])) \
        / compute_h0(three_x)

def compute_delta1(poly, three_x):
    return (plug_in_poly(poly, three_x[2]) \
        - plug_in_poly(poly, three_x[1])) \
        / compute_h1(three_x)

def compute_a(poly, three_x):
    delta0 = compute_delta0(poly,three_x)
    delta1 = compute_delta1(poly,three_x)

    h0 = compute_h0(three_x)
    h1 = compute_h1(three_x)
    
    return (delta1 - delta0) / (h1 + h0)

def compute_b(poly, three_x):
    a = compute_a(poly, three_x)
    h1 = compute_h1(three_x)
    delta1 = compute_delta1(poly, three_x)

    return a * h1 + delta1

def compute_c(poly, three_x):
    return plug_in_poly(poly, three_x[2])

def compute_delta(a, b, c):
    return b**2 - 4 * a * c

def compute_quad_roots(a, b, c):
    delta_squared = compute_delta(a, b, c) ** (0.5)
    return (b + delta_squared, b - delta_squared)

def compute_delta_x_muller(a, b, c):
    return (2 * c) / max(compute_quad_roots(a, b, c))

def insert_root(solution, candidate_root, e):
    for root in solution:
        if abs(root - candidate_root) <= e:
            return False
    solution.append(candidate_root)



# SECANT METHOD

def g(poly, x, h):
    return (3 * plug_in_poly(poly, x) \
        - 4 * plug_in_poly(poly, x - h) \
        + plug_in_poly(poly, x - 2 * h)) \
        / (2 * h)

def compute_delta_x_secant(x0, x1, poly, h):
    num =  g(poly, x1, h) - g(poly, x0, h)
    return (num, (x1 - x0) * g(poly, x1, h) / num)

def is_min_point(poly, x, h):
    double_deriv = (- plug_in_poly(poly, x + 2 * h) \
            + 16 * plug_in_poly(poly, x + h) \
            - 30 * plug_in_poly(poly, x) \
            + 16 * plug_in_poly(poly, x - h) \
            - plug_in_poly(poly, x - 2 * h)) \
            / 12 * (h ** 2)
    return double_deriv > 0