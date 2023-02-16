n = int(input())

data = [list(map(int,input().split())) for _ in range(n)]

data.sort(key = lambda x : (x[1],x[0]))

cnt = 1
tmp = data[0][1]

for i in data:
    if tmp <= i[0]:
        cnt += 1
        tmp = i[1]
print(cnt)