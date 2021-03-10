def DFS(L):
    global cnt
    if L == n:
        cnt += 1
        # for i in arr:
        #     print(i, end=' ')

        print()
    else:
        for i in range(1, n + 1):
            if ch[i] == 0 and g[L][i] == 1:
                ch[i] = 1
                arr.append(i)
                DFS(i)
                arr.pop()
                ch[i] = 0


n, m = map(int, input().split())

g = [[0] * (n + 1) for _ in range(n + 1)]
ch = [0] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    g[x][y] = 1
cnt = 0
arr = []
arr.append(1)
ch[1] = 1
DFS(1)
print(cnt)
