n = int(input())

data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key = lambda x : (x[0],x[1]))
print(data)
cnt = 0

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i][1] < data[j][1]:
            break
    else:
        cnt += 1
print(cnt)