l = int(input())
data = list(map(int,input().split()))
m = int(input())

for i in range(m):
    data.sort()
    data[0] = data[0] + 1
    data[-1] = data[-1] - 1
data.sort()
print(data[-1]-data[0])