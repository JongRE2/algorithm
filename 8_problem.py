def reverse(x):

    res=0
    while x>0:
        res=10*res+(x%10)
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2,(x//2)+1):
        if x%i==0:
            return False
    return True



n = int(input())
arr = list(map(int, input().split()))

for i in arr:
    tmp=reverse(i)
    if isPrime(tmp):
        print(tmp,end=' ')

