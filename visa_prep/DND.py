def c_d(n,m,arr):
    num1=0
    num2=0
    for number in arr:
        if number%m==0:
            num2+=number
        else:
            num1+=number
    return num2-num1
n,m=map(int, input().strip().split())
arr=list(map(int, input().strip().split()))
res=c_d(n,m,arr)
print(res)
