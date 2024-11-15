n=int(input())
c=1
for i in range(1,n+1):
    r=[]
    for j in range(i):
        r.append(c)
        c+=1
    print(" ".join(map(str,r)))
