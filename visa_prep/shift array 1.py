n=int(input())
arr=list(map(int, input().split()))
def r_a(arr):
    return arr[1:]+arr[:1]
roa=r_a(arr)
print(" ".join(map(str, roa)))
