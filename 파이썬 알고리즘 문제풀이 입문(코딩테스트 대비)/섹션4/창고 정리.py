l = int(input())
data = list(map(int, input().split()))
m = int(input())

for i in range(m):
    data[data.index(max(data))] = data[data.index(max(data))] - 1
    data[data.index(min(data))] = data[data.index(min(data))] + 1
print(max(data)-min(data))
