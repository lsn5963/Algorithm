k,n = map(int, input().split())
data = [int(input()) for _ in range(k)]

lt = 1
rt = max(data)
rst = 0
while lt<=rt:

    mid = (lt+rt)//2
    tot = 0
    for i in data:
        tot += i //mid

    if tot >= n:
       rst = mid
       lt = mid + 1
    else:
        rt = mid - 1
print(rst)