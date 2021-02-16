n = int(input())
min = 2147000000
arr = list(map(int, input().split()))
ave = int((sum(arr) / n) + 0.5)

for idx, x in enumerate(arr):
    tmp = abs(ave - x)
    if tmp < min:
        min = tmp
        st_x = x
        st_idx = idx
    elif tmp == min:
        if x > st_x:
            st_x = x
            st_idx = idx
print("%d %d" % (ave, st_idx + 1))
