def DFS(v):
    if v > num:
        for i in range(1,num+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)


num=int(input())
ch=[0]*(num+1)
DFS(1)
