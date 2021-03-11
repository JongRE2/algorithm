
def DFS(L,weight,time):
    global res
    if time > m:
        return
    if L==n:
        if res < weight:
            res=weight
    else:
        DFS(L+1,weight+pw[L],time+pt[L])
        DFS(L + 1, weight, time)


n,m=map(int,input().split())

res=-2147000000
pw=[]
pt=[]
for i in range(n):
    a,b=map(int,input().split())
    pw.append(a)
    pt.append(b)
DFS(0,0,0)

print(res)