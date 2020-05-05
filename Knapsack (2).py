import numpy
def maxGold(W, n, w) :
    table = numpy.zeros((W + 1, n + 1))
    for i in range(1, W + 1) :
        for j in range(1, n + 1) :
            table[i][j] = table[i][j - 1]
            if w[j - 1] <= i :
                val = table[i - w[j - 1]][j - 1] + w[j - 1]
                if val > table[i][j] :
                    table[i][j] = val
    return int(table[W][n])



W, n = [int(i) for i in input().split()]
w = [int(i) for i in input().split()]
print(maxGold(W, n, w))
