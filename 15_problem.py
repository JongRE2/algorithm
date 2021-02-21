
a,b=map(int,input().split())
arr=list(map(int,input().split()))
num=0
sum=0
cnt=0
for i in range(a):
    j=i
    sum=0
    while(j<a):
        sum+=arr[j]
        if (sum==b):
            cnt+=1
            break
        elif (sum<b):
            j+=1
            continue
        elif (sum>b):
            break
print(cnt)







