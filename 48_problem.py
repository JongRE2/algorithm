
def DFS(L):
    global cnt
    if L==m:
        for i in range(L):
            print(res[i],end=' ')
        cnt+=1
        print()
    else:
        for j in range(1,n+1):
            if ch[j]==0:
                ch[j]=1
                res[L]=j
                DFS(L+1)
                ch[j]=0

n,m=map(int,input().split())
res=[0]*m
ch=[0]*(n+1)
cnt=0
DFS(0)
print(cnt)