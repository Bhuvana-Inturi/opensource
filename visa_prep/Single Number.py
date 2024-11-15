n=int(input())
arr=list(map(int, input().split()))
r=0
for num in arr:
    r^=num
print(r)
