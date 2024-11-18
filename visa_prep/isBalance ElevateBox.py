n=int(input())
a=list(map(int, input().split()))
t_s=sum(a)
l_s=0
b_a=[]
for i in range(n):
    r_s=t_s-l_s-a[i]
    b=abs(l_s-r_s)
    b_a.append(b)
    l_s+=a[i]
print(" ".join(map(str,b_a)))
