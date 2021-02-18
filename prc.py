num1=int(input())
arr1=list(map(int,input().split()))
num2=int(input())
arr2=list(map(int,input().split()))
arr3=[10]*(num1+num2)
# print(arr3)
a=0
b=0
cnt=0

for i in range(num1+num2):

    if (a == num1):
        for j in range(b, num2):
            arr3[cnt] = arr2[b]
            cnt += 1
            b += 1
        break
    if (b == num2):
        for j in range(a, num1):
            arr3[cnt] = arr1[a]
            cnt += 1
            a += 1
        break
    if(arr1[a]<=arr2[b]):
        arr3[cnt]=arr1[a]
        a+=1

        # print(arr3)
    else:
        arr3[cnt]=arr2[b]
        b+=1
        # print(arr3)

    cnt+=1
for i in range(num1+num2):
    print(arr3[i],end=" ")
