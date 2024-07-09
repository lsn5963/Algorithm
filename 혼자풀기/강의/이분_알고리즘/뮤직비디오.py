n,m = map(int, input().split())
data = list(map(int, input().split()))
lt = 1
rt = sum(data)
mmax = max(data)
rst = 0
while lt <= rt:
    mid = (lt+rt)//2
    s = 0
    cnt = 1
    for i in data:
        if s+i<=mid:
            s += i
        else:
            s = i
            cnt += 1

    if mid >= mmax and cnt <= m:
        rst = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(rst)