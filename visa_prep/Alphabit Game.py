def cvandc(s):
    v="aeiouAEIOU"
    num_v=0
    num_c=0
    for char in s:
        if char.isalpha():
            if char in v:
                num_v+=1
            else:
                num_c+=1
    return num_v, num_c
i_s=input().strip()
v,c=cvandc(i_s)
print(f"{v},{c}")
