import copy
# from econ_utils import *
class Econ:
    def __init__(self, h=1):
        self.h = h
        self.mat = []
        for i in range(h):
            self.mat += [[]]

    def display(self):
        print("[")
        for line in self.mat:
            print("  ", line)
        print("]")

    def transpose(self):
        result = Econ(self.h)
        for line in range(self.h):
            for elem in self.mat[line]:
                result.add_elem(elem[0], elem[1], line)
        return result


    def get_elem(self, line, col, bisect=False):
        if bisect:
            vec = self.mat[line]
            i_begin = 0
            i_end = len(vec) - 1
            i_search = (i_begin + i_end) // 2
            while vec[i_search][1] != col:
                if vec[i_search][1] > col:
                    i_begin = i_search
                    i_search = (i_begin + i_end) // 2
                else:
                    i_end = i_search
                    i_search = (i_begin + i_end) // 2

            if vec[i_search][1] == col:
                return vec[i_search][0]
            else:
                return 0

        else:
            for pair in self.mat[line]:
                if pair[1] == col:
                    return pair[0]
            return 0

    def sort(self):
        for line in self.mat:
            line.sort(key=lambda x: x[1])

    def __getitem__(self, key):
        return self.get_elem(key[0], key[1])

    def add(self, other):
        result = copy.deepcopy(self)
        for line_i in range(len(other.mat)):
            for elem in other.mat[line_i]:
                val = elem[0]
                col_i = elem[1]
                result.add_elem(val, line_i, col_i)
        return result

    def multiply_mat(self, other):
        import time
        starting = time.time()
        result = Econ(h=self.h)
        other_t = other.transpose()
        n = self.h
        self.sort()
        other_t.sort()

        for line_r in range(n):
            # print('new line', line_r, '/', n)
            for col_r in range(n):
                val = 0
                v0 = self.mat[line_r]
                v1 = other_t.mat[col_r]
                iv0, iv1 = 0, 0
                while iv0 < len(v0) and iv1 < len(v1):
                    if v0[iv0][1] == v1[iv1][1]:
                        # if coinciding
                        val += v0[iv0][0] * v1[iv1][0]
                        iv0 += 1
                        iv1 += 1
                    elif v0[iv0][1] > v1[iv1][1]:
                        # v0 idx larger
                        iv1 += 1
                    elif v0[iv0][1] < v1[iv1][1]:
                        # v1 idx larger
                        iv0 += 1
                if val == 0:
                  continue
                result.mat[line_r].append([val, col_r])
#                result.add_elem(val, line_r, col_r)  
        print('Time:', time.time() - starting)
        return result

        
    def multiply_vec(self, vec):
        result = []
        n = self.h
        for col_r in range(n):
            val = 0
            for i in range(n):
                val += self.get_elem(col_r, i) * vec[i]
            result.append(val)
        return result

        
    def add_elem(self, x, line, col):
        # print("adding, elem at {}, {}: {} + {}".format(line, col, self.get_elem(line, col), x))
        if self.get_elem(line, col) == 0:
            self.mat[line] += [[x, col]]
        else:
            for i, elem in enumerate(self.mat[line]):
                if elem[1] == col:
                    if x > 0:
                        elem[0] += x
                    else:
                        del self.mat[line][i]

if __name__ == '__main__':
    print('debugging')
    # a = Econ(2)
    # a.add_elem(2, 0, 1)
    # a.add_elem(1, 0, 0)

    # eye2 = Econ(2)
    # eye2.add_elem(2, 0, 0)
    # # eye2.add_elem(2, 0, 1)
    # # eye2.add_elem(2, 1, 0)
    # eye2.add_elem(2, 1, 1)

    # vec = [10, 20]

    # a.display()
    # a.sort()
    # a.display()
    # a.transpose().display()
    
    # # eye2.display()
    # # a.multiply_mat(eye2).display()
    # # print(a.multiply_vec(vec))


    # 1 2  *  3 0  =  3 12
    # 3 4     0 6     9 24
