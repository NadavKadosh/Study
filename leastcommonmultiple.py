def lcm(a, b):
    return int((a*b)/(gcd(a,b)))
def gcd(a, b):
    while b!= 0:
        r = a%b
        a = b
        b = r
    return a

n =input()
a, b = map(int, n.split())
print(lcm(a, b))

