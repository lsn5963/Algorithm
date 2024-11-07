h,w = map(int,input().split())
data = list(map(int,input().split()))
cnt = 0
for i in range(1,w-1):
    # print(cnt)
    lm = max(data[:i])
    rm = max(data[i+1:])
    water = min(lm,rm)
    tmp = water - data[i]
    if tmp>0:
        cnt += tmp
print(cnt)