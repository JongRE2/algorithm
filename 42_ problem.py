
def DFS(n):
    if(n>7):
        return

    DFS(2*n)
    DFS(2*n+1)
    print(n, end=' ')

num=int(input())
DFS(num)

