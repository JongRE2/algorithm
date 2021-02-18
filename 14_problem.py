num1=input()
a=list(map(int,input().split()))
num2=input()
b=list(map(int,input().split()))
arr=a+b
arr.sort()

for i in arr:
    print(i, end=' ')
