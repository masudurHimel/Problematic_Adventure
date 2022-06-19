import time
import cython


def generate(numRows: cython.int):
    res = [[1], [1, 1]]
    for i in range(2, numRows):
        res.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                res[i].append(1)
            else:
                res[i].append(sum(res[i - 1][j - 1:j + 1]))

    return res


start_time = time.time()
_ = generate("5000")
print(time.time() - start_time)
