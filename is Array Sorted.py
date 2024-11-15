def sorted(n,arr):
  for i in range(1,n):
      if arr[i]<arr[i-1]:
            return "false"
  return "true"
n=int(input())
arr=list(map(int, input().split()))
print(sorted(n,arr))
