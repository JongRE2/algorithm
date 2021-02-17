arr=list(range(21))

for _ in range(10):
    a,b=map(int,(input().split()))
    for j in range((b-a+1)//2):
        arr[a+j],arr[b-j]=arr[b-j],arr[a+j]

arr.pop(0)
for x in arr:
    print(x,end=" ")
