n,x = map(int,input().split())
data = list(map(int,input().split()))
cnt = 1
lt = 0
rt = x
tmp = sum(data[:rt])
total = sum(data[:rt])
for i in range(1,n-x+1):
    tmp = tmp-data[lt] + data[rt]
    # print("z",tmp)
    lt += 1
    rt += 1
    if tmp == total:
        cnt += 1
    if tmp > total:
        total = tmp
        cnt = 1

if total == 0:
    print("SAD")
else:
    print(total)
    print(cnt)