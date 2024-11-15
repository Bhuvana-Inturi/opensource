
n=int(input())
a=list(map(int, input().split()))
k=int(input())
s=set()
f=False
for num in a:
    if k-num in s:
        f=True
        break
    s.add(num)
if found:
    print("True")
else:
print("False")
