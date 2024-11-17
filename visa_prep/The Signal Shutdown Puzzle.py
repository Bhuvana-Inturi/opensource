def fg(n,m,g):
    rz=set()
    cz=set()
    for i in range(n):
        for j in range(m):
            if g[i][j]==0:
                rz.add(i)
                cz.add(j)
    for i in range(n):
        for j in range(m):
            if i in rz or j in cz:
                g[i][j]=0
    for r in g:
        print(" ".join(map(str, r)))
n,m=map(int, input().split())
g=[list(map(int, input().split())) for _ in range(n)]
fg(n,m,g)
