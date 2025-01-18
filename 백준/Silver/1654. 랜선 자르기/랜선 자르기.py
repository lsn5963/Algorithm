k,n = map(int, input().split())
data = [int(input()) for _ in range(k)]

lt = 1
rt = max(data)
rst = 0
while lt<=rt:
    mid = (lt+rt)//2
    cnt = 0
    for i in data:
        cnt += i // mid
    # print(mid,lt,rt,cnt)

    if cnt >= n:
        rst = mid
        lt = mid + 1
    else:
        rt = mid - 1


print(rst)