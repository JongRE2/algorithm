n=int(input())

arr=list(map(int,input().split()))
arr2=[0]*(n)

value=[0]*(n+1)
max=-2147000000
max_idx=0
for j in range(n):
    arr2[j]=arr[j]
for i in range(n):
    while arr[i]>0:
        value[i]+=arr[i]%10
        arr[i]=arr[i]/10
    if max < value[i]:
        max=value[i]
        max_idx=i
print(arr2[max_idx])