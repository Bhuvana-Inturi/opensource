n=int(input())
m=[list(map(int, input().split())) for i in range(n)]
t=[[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        t[i][j]=m[j][i]
for row in t:
    print(" ".join(map(str, row)))
