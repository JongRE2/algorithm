
import sys
def DFS(w,i):
    global sum
    if w > c:
        return
    if i==n:
        if w>sum:
            sum=w
    else:
        DFS(w + a[i], i + 1)
        DFS(w, i + 1)


c,n=map(int,input().split())
a=[0]*(n+1)
for i in range(n):
    a[i]=int(input())
sum=-1
DFS(0,0)
print(sum)
