def max_tp(n,sti):
    sti.sort(reverse=True)
    for i in range(n-2):
        a,b,c=sti[i],sti[i+1],sti[i+2]
        if a<b+c:
            return a+b+c
    return -1
n=int(input())
sti=list(map(int, input().split()))
print(max_tp(n,sti))
