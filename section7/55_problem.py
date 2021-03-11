def DFS(L, w):
    global res
    if L == n + 1:
        if w > res:
            res = w
    else:
        if L + day[L] <= n + 1:
            DFS(L + day[L], w + work[L])
        DFS(L + 1, w)


n = int(input())

day = []
work = []
res = -2147000000
for i in range(n):
    a, b = map(int, input().split())
    day.append(a)
    work.append(b)
day.insert(0, 0)
work.insert(0, 0)
# print(day)
DFS(1, 0)
print(res)