n,m =  map(int, input().split())

data = list(map(int, input().split()))
sum = 0
cnt = 0
data.sort()
lt = 0
rt = len(data)-1
print(data)
while lt<=rt:
    if data[lt] + data[rt] <= m:
        cnt += 1
        lt += 1
        rt -= 1
    else:
        rt -= 1
print(cnt)
print(len(data)-(cnt*2) + cnt)
