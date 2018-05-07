from lib import *

def get_input_params():
    with open("input_params_secant.txt") as f:
        fst_line = f.readline().split()
        domain = (int(fst_line[0]), int(fst_line[1]))
        h = float(fst_line[2])
        iters = int(fst_line[3])
        e = float(fst_line[4])
        kmax = int(fst_line[5])
        poly = np.loadtxt(f)
        return (domain, iters, h, e, kmax, poly)

domain, iters, h, e, kmax, poly = get_input_params()

solution = []

while iters != 0:
    x0, x1 = get_initial_values(domain, 2)
    x = x1
    print(f"For x0: {x0}, x1: {x1} we have:")
    delta_x = e + 1
    k = 0

    while True:
        delta_x_num, delta_x = compute_delta_x_secant(x0, x1, poly, h, g1)
        
        if abs(delta_x_num) <= e:
            delta_x = 10**(-5)

        x = x - delta_x
        k = k + 1
        x0 = x1
        x1 = x

        if not (abs(delta_x) >= e and k <= kmax and abs(delta_x) <= 10**8):
                break

    if abs(delta_x) < e:
        if is_min_point(poly, x, h):
            print(f"min point: {x}", end="\n\n")
            insert_root(solution, x, e)
    else:
        print("divergent", end="\n\n")

    iters = iters - 1

print("Domain", domain)
print("Solution", solution)