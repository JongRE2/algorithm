dx=[-1,0,1,0]
dy=[0,1,0,-1]
num=int(input())
cnt=0
arr=[list(map(int,input().split())) for _ in range(num)]
arr.insert(0,[0]*num)
arr.append([0]*num)
for i in arr:
    i.append(0)
    i.insert(0,0)
for i in range(1,num+1):
    for j in range(1,num+1):
        if all(arr[i][j]>arr[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1
print(cnt)



