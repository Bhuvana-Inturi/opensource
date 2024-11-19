n=int(input())
matrix=[list(map(int, input().split())) for _ in range(n)]
res=[]
for i in range(n):
    r_s=sum(matrix[i])
    c_s=sum(matrix[j][i] for j in range(n))
    res.append(r_s+c_s)
print(" ".join(map(str, res)))
