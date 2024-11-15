n=int(input())
m=[]
for _ in range(n):
    r=list(map(int, input().split()))
    m.append(r)
m_i=[r[::-1] for r in m]
for r in m_i:
    print(*r)
