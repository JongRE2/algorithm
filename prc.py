num=int(input())


for i in range(num):
    arr=input()
    arr=arr.upper()
    size=len(arr)
    chk = 0
    for j in range((size//2)):
        if (arr[j] == arr[(size - 1) - j]):
            continue
        else:
            chk = 1
            print("#%d NO" %(i+1))
            break
    if(chk==0):
        print("#%d YES" %(i+1))
