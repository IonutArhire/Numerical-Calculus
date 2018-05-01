from lib import *

def get_input_params():
    with open("input_params_muller.txt") as f:
        fst_line = f.readline().split()
        iters = int(fst_line[0])
        e = float(fst_line[1])
        kmax = int(fst_line[2])
        poly = np.loadtxt(f)
        return (iters, e, kmax, poly)

iters, e, kmax, poly = get_input_params()

domain = get_domain(poly)

solution = []

while iters != 0:
    three_x = get_initial_values(domain, 3)
    print(f"For x0: {three_x[0]}, x1: {three_x[1]}, x2: {three_x[2]} we have:")
    delta_x = e + 1
    k = 0

    while True:
        a = compute_a(poly, three_x)
        b = compute_b(poly, three_x)
        c = compute_c(poly, three_x)

        if compute_delta(a, b, c) < 0:
            break

        quadtratic_roots = compute_quad_roots(a, b, c)
        if abs(max(quadtratic_roots[0], quadtratic_roots[1])) < e:
            break

        delta_x = compute_delta_x_muller(a, b, c)
        new_x = three_x[2] - delta_x

        k = k + 1
        three_x[0] = three_x[1]
        three_x[1] = three_x[2]
        three_x[2] = new_x

        if not (abs(delta_x) >= e and k <= kmax and abs(delta_x) <= 10**8):
            break

    if abs(delta_x) < e:
        print(f"root: {three_x[2]}", end="\n\n")
        insert_root(solution, three_x[2], e)
    else:
        print("divergent", end="\n\n")

    iters = iters - 1

print("Domain", domain)
print("Solution", solution)

with open("found_roots.txt", mode='w') as f:
    f.write(str(solution))