num=int(input())

a=[list(map(int,input().split())) for _ in range(num)]

s=e=num//2
sum=0
for i in range(num):
    for j in range(s,e+1):
        #print(a[i][j])
        sum+=a[i][j]
    if(i<(num//2)):
        s-=1
        e+=1
    else:
        s+=1
        e-=1

print(sum)