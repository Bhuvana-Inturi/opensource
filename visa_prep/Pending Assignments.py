x,y,z=map(int, input().split())
tr=x*y
ta=z*1440
if tr<=ta:
    print("YES")
else:
    print('NO')
