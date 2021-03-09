import sys

def DFS(L):
    global sum
    if L==n:
        for i in range(n):
            sum+=arr[i]*b[i]
        if sum==f:
            for j in range(n):
                print(arr[j],end=' ')
            sys.exit(0)
        else:
            sum=0
    else:
        for i in range(1,n+1):
            if ch[i]==0:
                arr[L]=i
                ch[i]=1
                DFS(L+1)
                ch[i]=0

n,f=map(int,input().split())
arr=[0]*n
b=[1]*n
for i in range(1,n):
    b[i]=b[i-1]*(n-i)//i
sum=0
ch=[0]*(n+1)
# for i in b:
#     print(i,end=' ')
DFS(0)
#print(b)