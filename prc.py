arr=[list(map(int,input().split())) for _ in range(7)]
size=len(arr)-1
cnt2=0
for i in range(7):
    for j in range(3):
        cnt0 = 0
        cnt1 = 0
        for k in range(j,j+(5 // 2)):
            if (arr[i][k] == arr[i][size - k]):
                cnt0 += 1
            if (arr[k][i] == arr[size-k][i]):
                cnt1 += 1
        if (cnt0 == 2):
            cnt2 += 1
        if (cnt1 == 2):
            cnt2 += 1
print(cnt2)
