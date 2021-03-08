
def DFS(b,cnt):
    global summ
    global minn
    if cnt >minn:
        return
    if money<b:
        return
    if b==money:
        if minn > cnt:
            minn=cnt
            return
    else:
        for i in range(n):
            DFS(b+arr[i],cnt+1)



n=int(input())
arr=list(map(int,input().split()))
arr.sort(reverse=True)
money=int(input())
minn=1000000
DFS(0,0)
print(minn)
