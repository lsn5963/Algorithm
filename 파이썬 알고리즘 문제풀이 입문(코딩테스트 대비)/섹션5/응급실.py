from collections import deque
n,m = map(int, input().split())

data = list(map(int, input().split()))
data = deque(data)
cnt = 0
check = True
data[m] = str(data[m])
find = data[m]
while data:
    tmp = data.popleft()
    for i in data:
        if int(i) > int(tmp):
            data.append(tmp)
            break
    else:
        cnt += 1
        if tmp == find:
            check = False

    if check == False:
        break

# enumerate사용해서 풀어야함
        
print(cnt)