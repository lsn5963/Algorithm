n,c = map(int, input().split())

data = [int(input()) for _ in range(n)]
data.sort()


lt = min(data)
rt = max(data)

def Count(mid):
    cnt = 1
    tmp = min(data)
    for i in range(1,n):
        if data[i] - tmp >= mid:
            cnt += 1
            tmp = data[i]
    return cnt
while lt<=rt:
    mid = (lt+rt)//2

    if Count(mid) >= c:
        lt = mid + 1
        res = mid 
    else:
        rt = mid -1
print(res)
    
    