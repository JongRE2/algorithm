def DFS(a):
    global cnt
    if a==m:
        for j in range(m):
            print(arr[j],end=' ')
        print()
        cnt += 1
        return
    for i in range(1,n+1):
        arr[a]=i
        DFS(a+1)



n,m=map(int,input().split())

arr=[0]*m
cnt=0
DFS(0)
print(cnt)
