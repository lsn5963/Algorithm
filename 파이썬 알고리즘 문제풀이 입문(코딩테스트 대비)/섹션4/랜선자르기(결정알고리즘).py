k,n = map(int, input().split())

data = [int(input()) for _ in range(k)]

lt = 1
rt = max(data)
while lt<=rt:
    mid = (lt+rt)//2
    sum = 0
    for i in data:
        sum += i // mid
        
    if sum >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid -1
print(res)