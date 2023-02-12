n,m = map(int, input().split())

data = list(map(int, input().split()))
count = 0

lt, rt = 0, 1
sum = data[0]
while True:
    if sum < m:
        if rt < n:
            sum += data[rt]
            rt += 1
        else:
            break
    elif sum == m:
        sum -= data[lt]
        lt += 1
        count += 1
    else:
        sum -= data[lt]
        lt += 1
            

print(count)