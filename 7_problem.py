n = int(input())
main = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, i):

        if i % j == 0:
            cnt += 1
    if cnt == 1:
        main += 1
print(main)
