
import sys
def DFS(L,sum,tsum):
    global result
    if sum+(total-tsum)<result:
        return
    if sum > c:
        return
    if L==n:
        if sum>result:
            result=sum
    else:
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,tsum+a[L],tsum+a[L])


c,n=map(int,input().split())
a=[0]*(n)
for i in range(n):
    a[i]=int(input())
result=-1
total=sum(a)
DFS(0,0,0)
print(result)
