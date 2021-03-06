import sys
def DFS(i,sum):
    if sum>total//2:
        return
    if i==num:
        if sum==total-sum:
            print("YES")
            sys.exit(0)
    else:
        DFS(i+1,sum+a[i])
        DFS(i + 1, sum)


num=int(input())
a=list(map(int,input().split()))
total=sum(a)
DFS(0,0)
print("NO")