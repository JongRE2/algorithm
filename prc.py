test=int(input())
cnt=0
while(cnt<test):
    cnt+=1
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s - 1:e]
    arr.sort()
    print('\n')
    print("#%d %d" %(cnt,arr[k - 1]))