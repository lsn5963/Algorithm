n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data.sort(key = lambda x : x[1])
# print(data)
cnt = 0
s = data[0][0]
t = data[0][1]

for i in range(1,len(data)):
    if data[i][0]>=t:
        # print(data[i][0])
        t = data[i][1]
        cnt += 1

print(cnt+1)
