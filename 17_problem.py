num=int(input())

arr=[list(map(int,input().split())) for _ in range(num)]
arr.insert(0,[0]*num)
arr.append([0]*num)
for i in arr:
    i.append(0)
    i.insert(0,0)
# for j in arr:
#     print(j)
cnt=0
x=[-1,0,1,0]
y=[0,1,0,-1]
for a in range(1,num+1):
    for b in range(1,num+1):
        stand=arr[a][b]
        if(stand>arr[a-1][b] and stand>arr[a][b+1] and stand>arr[a+1][b] and stand>arr[a][b-1]):
            cnt+=1
print(cnt)

