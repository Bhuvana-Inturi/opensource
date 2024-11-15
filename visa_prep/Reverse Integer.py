
n=int(input())
i_min,i_max=-2**31, 2**31-1
is_neg=n<0
n=abs(n)
reversed_n=int(str(n)[::-1])
if is_neg:
    reversed_n=-reversed_n
if reversed_n<i_min or reversed_n>i_max:
    print(0)
else:
    print(reversed_n)
