n, m = map(int, input().split())
data = list(map(int, input().split()))


lt = max(data)
rt = sum(data)
rst = 0
while lt<=rt:
    count = 1
    sum = 0
    mid = (lt+rt)//2
    for i in data:        
        if sum + i > mid:
            count += 1
            sum = 0
        sum += i
    if count <= m:
        rst = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(rst)        