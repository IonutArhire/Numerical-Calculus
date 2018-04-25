from econ import Econ
def read_file(filename, warn_nonzero=False):
    # file looks like: 
    #0 3
    #1 
    #2 11
    #3 22
    #4 33
    #5
    #6 elem, line, col
    #x...
    #
    with open(filename, 'r') as f:
        data = f.read().split('\n')
    size = int(data[0])
    # vector: 2 to size+2
    vec = [float(x) for x in data[2:size+2]]
    # mat: size+3 to -1
    mat = Econ(size)
    mat_vec = [[float(y) for y in x.split(', ')] for x in data[size+3:-1]]
    # print(len(mat_vec), 'nonzeros')
    for elem in mat_vec:
        mat.add_elem(elem[0], int(elem[1]), int(elem[2]))
    if warn_nonzero:
        for i, line in enumerate(mat.mat):
            if len(line) > 10:
                print('more than 10 nonzero elements on line {}'.format(i))
    return vec, mat

def equal_mats(a, b):
    if a.h != b.h:
        raise ValueError('differently sized matrices')
    h = a.h
    for line in range(h):
        for col in range(h):
            if abs(a.get_elem(line, col) - b.get_elem(line, col)) > 0.0001:
                return False
    return True

def equal_vecs(a, b):
    if len(a) != len(b):
        raise ValueError('differently sized vectors')
    for i in range(len(a)):
            if abs(a[i] - b[i]) > 0.0001:
                return False
    return True