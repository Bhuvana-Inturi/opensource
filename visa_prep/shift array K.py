x=int(input())
n=list(map(int, input().split()))
k=int(input())
k%=x
res=n[-k:]+n[:-k]
print(*res)
