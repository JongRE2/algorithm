a,b=map(int,input().split())

arr=list(map(int,input().split()))
arr.sort()
lt=0
rt=a-1
while(lt<=rt):
    mid = (lt + rt) // 2
    if (arr[mid]==b):
        print(mid+1)
        break
    elif (arr[mid]>b):
        rt=mid
    elif (arr[mid]<b):
        lt=mid+1

