n,m = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
print(data)
lt = 0
rt = len(data)-1
cnt = 0
while lt<=rt:
    print(data[lt]+data[rt])
    if data[lt]+data[rt] <= m:
        lt += 1
        rt -= 1
        cnt += 1
    else:
        cnt += 1
        rt -= 1
# print(len(data)-cnt)
print(cnt)