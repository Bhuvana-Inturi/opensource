n=int(input())
arr=list(map(int, input().split()))
def f_u(arr):
    seen=set()
    re=[]
    for num in arr:
        if num not in seen:
            seen.add(num)
            re.append(num)
    return re
u_e=f_u(arr)
print(" ".join(map(str, u_e)))
