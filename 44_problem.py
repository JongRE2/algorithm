
import sys

def DFS(i,sum):
    if(sum>total//2):
        return
    if(i==num):
        if sum==total-sum:
            print("YES")
            sys.exit(0)

    else:
        DFS(i + 1, sum + arr[i])
        DFS(i + 1, sum)


num=int(input())
arr=list(map(int,input().split()))
total=sum(arr)
DFS(0,0)
print("NO")
