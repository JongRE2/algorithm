arr=[list(map(int,input().split())) for _ in range(9)]

dx=[0,-1,-1,-1,0,0,1,1,1]
dy=[0,-1,0,1,-1,1,-1,0,1]

str=1
for i in arr:
    print(i)
for i in range(1,9,+3):

    for j in range(1,9,+3):
        checkin = list([0] * 10)
        for k in range(0,9):
            checkin[(arr[i+dx[k]][j+dy[k]])]=1
        if all(checkin[l]==1 for l in range(1,10)):
            continue
        else:
            str=0
for i in range(0,9):
    checkin1 = list([0] * 10)
    checkin2 = list([0] * 10)
    for j in range(0,9):
        checkin1[arr[i][j]] = 1
        checkin2[arr[j][i]] = 1

if all(checkin1[l]!=1 or checkin2[l]!=1 for l in range(1,10)):
    str=0

if str==1:
    print("YES")
elif str==0:
    print("NO")


