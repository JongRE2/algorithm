
def DFS(L,s,sum):
    global cnt
    if L==k:
        if sum%d==0:
            cnt+=1
    else:
        for i in range(s,n):
            DFS(L+1,i+1,sum+arr[i])


n,k=map(int,input().split())
arr=list(map(int,input().split()))
d=int(input())
cnt=0
DFS(0,0,0)
print(cnt)