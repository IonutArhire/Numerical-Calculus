import numpy as np
from econ import Econ
from econ_utils import *

# 1 2  * [10   =  [ 50
# 3 4     20]      110]
ex1 = Econ(2)
ex1.add_elem(1, 0, 0)
ex1.add_elem(2, 0, 1)
ex1.add_elem(3, 1, 0)
ex1.add_elem(4, 1, 1)

ex2 = Econ(2)
ex2.add_elem(3, 0, 0)
ex2.add_elem(6, 1, 1)

ex3 = [10, 20]
res_mv = [50, 110]

res_mm = Econ(2)
res_mm.add_elem(3, 0, 0)
res_mm.add_elem(12, 0, 1)
res_mm.add_elem(9, 1, 0)
res_mm.add_elem(24, 1, 1)

print('example 1', equal_mats(ex1.multiply_mat(ex2), res_mm))
print('example 2', equal_vecs(ex1.multiply_vec(ex3), res_mv))

v1, A = read_file('a.txt', warn_nonzero=True)
v2, B = read_file('b.txt', warn_nonzero=True)
v3, A_plus_B = read_file('aplusb.txt')
v4, A_ori_B = read_file('aorib.txt')

# for mat in [A, B, A_plus_B, A_ori_B]:
#     mat.sort()

series = [x for x in range(2018, 0, -1)]
print('vecmul A', equal_vecs(A.multiply_vec(series), v1))
print('vecmul B', equal_vecs(B.multiply_vec(series), v2))
print('A + B', equal_mats(A.add(B), A_plus_B))
# print 'starting'
print('A . B', equal_mats(A.multiply_mat(B), A_ori_B))
