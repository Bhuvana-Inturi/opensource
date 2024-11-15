import math
x,n=map(int, input().split())
c=x*100
if c>=n:
    print(0)
else:
    needed=math.ceil((n-c)/100)
    print(needed)
