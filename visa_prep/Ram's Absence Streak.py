n=int(input())
att=list(map(int, input().split()))
c_c=0
m_c=0
for day in att:
    if day==0:
        c_c+=1
    else:
        m_c=max(m_c,c_c)
        c_c=0
m_c=max(m_c,c_c)
print(m_c)
