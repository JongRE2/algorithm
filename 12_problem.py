#-48했을때 0~9범위
import math
def dividing(x):
    cnt=0
    for i in range(1,int(math.sqrt(x))+1):
        if x%i==0:
            cnt+=1
    return cnt*2
str=input()
size=len(str)
sum=0
for i in str:
    temp=ord(i)-48
    if temp>=0 and temp<=9:

            sum=10*sum+temp
print(sum)
print(dividing(sum))
