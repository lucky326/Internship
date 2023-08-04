n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def permutations(n, r):
    return factorial(n) / factorial(n - r)

def combinations(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

if(n>r):
    p=permutations(n,r)
    c=combinations(n,r)
    print("permutations are"+p)
    print("combinations are"+c)
else:
    print("n should be greater than r")