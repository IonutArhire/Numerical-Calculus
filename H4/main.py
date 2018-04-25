import numpy as np
from econ import Econ
from econ_utils import *

b, A = read_file('mock.txt', warn_nonzero=True)
# b, A = read_file('m_rar_2018_4.txt', warn_nonzero=True)
# b2, a2 = read_file('m_rar_2018_2.txt', warn_nonzero=True)
# b3, a3 = read_file('m_rar_2018_3.txt', warn_nonzero=True)
# b4, a4 = read_file('m_rar_2018_4.txt', warn_nonzero=True)
# b5, a5 = read_file('m_rar_2018_5.txt', warn_nonzero=True)
# print(b)
# A.display()
diff = 1
n = len(b)
# x_new = [1, 2, 3, 4, 5]
x_new = np.zeros(n)
print(A.check_diagonal())

while diff > 10 ** (-7):
    x_old = np.copy(x_new)
    for idx in range(n):
        x_i = b[idx]
        for i in range(n):
            if i != idx:
                x_i -= A.get_elem(idx, i) * x_new[i]
        x_i /= A.get_elem(idx, idx)
        x_new[idx] = x_i
    
    delta = np.linalg.norm(x_new - x_old)
    print('delta', delta)

    diff = np.linalg.norm(np.subtract(A.multiply_vec(x_new), b))
    print('final diff for Ax - b:', diff)
    if diff < 0.1:
        print('diff less than 0.1')
        print(x_new)