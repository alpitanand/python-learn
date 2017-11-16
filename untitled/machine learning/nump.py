from math import factorial
def solveaSmall(a, n, p):
    if(a==n==p):
        return 0

    # def range_prod(lo, hi):
    #     if lo + 1 < hi:
    #         mid = (hi + lo) // 2
    #         return range_prod(lo, mid) * range_prod(mid + 1, hi)
    #     if lo == hi:
    #         return lo
    #     return lo * hi
    #
    # def treefactorial(n):
    #     if n < 2:
    #         return 1
    #     return range_prod(1, n)
    # k=1
    # for i in range(1,n+1):
    #     k = k * i
    k = factorial(n)
    j = pow(a, k, p)
    return j

v = solveaSmall(99971, 99989, 99991)
print(v)
