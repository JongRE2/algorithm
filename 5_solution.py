#겨수님 풀이법
import sys
sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
cnt=[0]*(n+m+3) # +3을 한 이유는 그냥 공간을 좀더 넉넉히 하고싶어서 한다고하심
max=-2147000000
for i in range(1,n+1):
    cnt[i+j]+=1
for j in range(n+m+1):
    if cnt[i]>max:
        max=cnt[i]
for i in range(n+m+1):
    if cnt[i]==max:
        print(i,end=' ')
