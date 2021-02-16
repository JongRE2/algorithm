num=int(input())

arr=list(map(int,input().split()))
val=[0]*num
cnt=0
for i in range(num):
    if i==0:
        if arr[i]==1:
            cnt+=1
            val[i]=cnt
        elif arr[i]==0:
            cnt=0
            val[i]=cnt
    else:
        if arr[i-1]==1 and arr[i]==1:
            cnt+=1
            val[i]=cnt
        elif arr[i-1]==0:
            if arr[i]==1:
                cnt=1
                val[i]=cnt
            elif arr[i]==0:
                cnt=0
                val[i]=cnt
sum=0
for j in range(num):
    sum=sum+val[j]
print(sum)
