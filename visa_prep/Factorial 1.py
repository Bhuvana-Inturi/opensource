def fact(n):
    if n==0:
        return 1
    r=1
    for i in range(1,n+1):
        r*=i
    return r
n=int(input())
print(fact(n))
