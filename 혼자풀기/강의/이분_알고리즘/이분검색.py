n,m = map(int,input().split())
data = list(map(int,input().split()))

data.sort()
lt = 1
rt = len(data)
mid = 0
while True:
    mid = (lt + rt) // 2

    if data[mid] > m:
        rt = mid - 1
    elif data[mid] < m:
        lt = mid + 1
    else:
        print(mid+1)
        break