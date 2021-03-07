def DFS(i,w,pw):
    global maxx
    if w+(total-pw)<maxx:
        return
    if c<w:
        return
    if i==n:
        if maxx<w:
            maxx=w

    else:
        DFS(i+1,w+arr[i],pw+arr[i])
        DFS(i + 1, w,pw+arr[i])

c,n=map(int,input().split())

arr=[0]*n
for i in range(n):
    arr[i]=int(input())
maxx=-1
total=sum(arr)
DFS(0,0,0)
print(maxx)

# DFS(0,0,0,)