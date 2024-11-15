t=int(input().strip())
for _ in range(t):
    x,n=map(int, input().split())
    pc=x//10
    s=pc*n
    print(s)
