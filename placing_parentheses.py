import math
def evalt(a, b, op):
    if op == '+':
        r = a+b
        return r
    elif op == '-':
        r = a-b
        return r
    elif op == '*':
        r = a*b
        return r

def get_maximum_value(operands, operators):
    n = len(operands)
    m = [[None for x in range(n)] for x in range(n)]
    M = [[None for x in range(n)] for x in range(n)]
    for i in range(n):
        M[i][i] = operands[i]
        m[i][i] = operands[i]
    for s in range(1,n):
        for i in range(0,n-s):
            j = i + s
            m[i][j],M[i][j] = minandmax(M, m, i, j, operators)
    return M[0][n-1]

def minandmax(M, m, i, j, operators):
    maxi = -math.inf
    mini = math.inf
    for k in range(i,j):
        a = evalt(M[i][k], M[k+1][j], operators[k])
        b = evalt(M[i][k], m[k+1][j], operators[k])
        c = evalt(m[i][k], M[k+1][j], operators[k])
        d = evalt(m[i][k], m[k+1][j], operators[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return mini, maxi

the_input = input()
operators, operands = [], []

for i in the_input:
    if i in ['+', '-', '*']:
        operators.append(i)
    else:
        operands.append(int(i))
print(get_maximum_value(operands, operators))
