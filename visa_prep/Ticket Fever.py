t=int(input())
for _ in range(t):
    n,m=map(int, input().split())
    s=max(0,n-m)
    print(s)
