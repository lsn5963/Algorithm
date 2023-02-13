n, m = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

st = 0
ed = n-1

while st<=ed:
    mid = (ed+st) // 2
    if data[mid] > m:
        ed = mid - 1
    elif data[mid] == m:
        print(mid+1)
        break
    else:
        st = mid + 1