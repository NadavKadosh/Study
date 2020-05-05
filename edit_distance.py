# Uses python3
def edit_distance(s, t):
    table = [[]]
    s =" "+s
    t =" "+t
    for i in range(len(s)):
        table.append([])
        for j in range(len(t)):
            table[i].append(0)
    for i in range(len(s)):
        for j in range(len(t)):
            if i == 0:
                table[i][j] = j
            if j == 0:
                table[i][j] = i
    for i in range(1,len(s)):
        for j in range(1,len(t)):
            if i == 0:
                table[i][j] = j
            if j == 0:
                table[i][j] = i
            insertion = table[i][j-1] + 1
            deletion  = table[i-1][j] + 1
            mismatch  = table[i-1][j-1] + 1
            match     = table[i-1][j-1]
            if s[i] == t[j] and i != 0 and j != 0:
                table[i][j] = min(insertion, deletion, match)
            else:
                table[i][j] = min(insertion, deletion, mismatch)
    return table[len(s)-1][len(t)-1]

print(edit_distance(input(), input()))
