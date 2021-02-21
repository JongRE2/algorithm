num=int(input())

arr=[list(map(int,input().split())) for _ in range(num)]
arr2=arr
num2=int(input())

for _ in range(num2):
    a,b,c=map(int,input().split())
    arr2=arr[a-1]
    if(b==0):
        for i in range(0,num):
            if ((i+1)%c)!=0 :
                arr2[a-1][i-c]=arr[a-1][i]

            elif (i+1)%c==0:
                tmp=(i+1)-c
                arr2[(a-1)][(num-1)-tmp]=arr[(a-1)][i]
    arr[(a-1)]=arr2[(a-1)]
print(arr)



