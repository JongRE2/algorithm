num=int(input())

for i in range(num):
    st=input()
    st=st.upper()
    size=len(st)
    for j in range(size//2):
        if st[j]!=st[(size-1)-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" % (i + 1))

