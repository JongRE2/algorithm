num=int(input())

arr=[list(map(int,input().split())) for _ in range(num)]

a=b=num//2
sum=0
for i in range(num):
    for j in range(a,b+1):
       sum+=arr[i][j]
    if (i < (num // 2)):
        a-=1
        b+=1
    else:
        a+=1
        b-=1

print(sum)

