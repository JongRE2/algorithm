
a,b=map(int,input().split())

cnt=0
str=0
for i in range(1,a+1):
    if(a%i==0):
        cnt+=1
        if(cnt==b):
            str=i
            print(str)
            break
if(cnt<b):
    print(-1)
