Case=int(input())

for t in range(Case):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e]
    a.sort()
    print("\n#%d %d" %(t+1,a[k-1]))
