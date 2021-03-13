
def DFS(L,sum):
    global total
    if L==n+1:
        if sum>total:
            total=sum
    else:
        if L+t[L] <=n+1 :
            DFS(L+t[L],sum+p[L])
        DFS(L+1,sum)



n=int(input())
t=list()
p=list()
total=-2147000000
for i in range(n):
    a,b=map(int,input().split())
    t.append(a)
    p.append(b)
t.insert(0,0)
p.insert(0,0)

DFS(1,0)
print(total)