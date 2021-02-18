s=input()
res=0
for x in s:
    if x.isdecimal():
        res=int(x)
print(res)

cnt=0
for i in range(1,res+1):
    if res%i==0:
        cnt+=1
print(cnt)
# g0en2Ts8eSoft
