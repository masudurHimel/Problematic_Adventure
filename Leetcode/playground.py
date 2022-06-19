import time


def generate(numRows):
    res = [[1], [1, 1]]
    for i in range(2, numRows):
        res.append([])
        for j in range(i + 1):
            if j == 0 or j == i:
                res[i].append(1)
            else:
                res[i].append(sum(res[i - 1][j - 1:j + 1]))

    return res



