num=int(input())

arr=[list(map(int,input().split())) for _ in range(num)]
# print(arr)
num2=int(input())

for i in range(num2):
    a,b,c=map(int,input().split())
    if(b==0):
        for _ in range(c):
            arr[a - 1].append(arr[a - 1].pop(0))
    elif(b==1):
        for _ in range(c):
            arr[a-1].insert(0,arr[a-1].pop())
# print(arr,end=" ")

a=0
b=num
sum=0
for i in range(num):
    print(a, b)
    for j in range(a,b):
        sum+=arr[i][j]
    if (i < (num // 2)):
        a+=1
        b-=1
    elif(i>=(num//2)):
        a-=1
        b+=1
print(sum)

