import random
def partition3(a, l, r):
    x = a[l]
    right = l
    for i in range(l + 1, r + 1) :
        if a[i] <= x :
            right += 1
            a[i], a[right] = a[right], a[i]
    if right != l:
        a[l], a[right] = a[right], a[l]
    left = right
    for i in range(right - 1, l - 1, -1) :
        if a[i] == x :
            left -= 1
            a[i], a[left] = a[left], a[i]
    if left != l:
        a[l], a[left - 1] = a[left - 1], a[l]
    return a, left, right

def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    a, left, right = partition3(a, l, r)
    randomized_quick_sort(a, l, left)
    randomized_quick_sort(a, right+1, r)

n = int(input())
a = list(map(int, input().split()))
randomized_quick_sort(a, 0, n - 1)
for x in a:
    print(x, end=' ')
