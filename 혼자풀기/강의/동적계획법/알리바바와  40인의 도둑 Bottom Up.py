from collections import deque
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1]
dy = [1,0]
q = deque()
q.append((0,0))
for i in range(n):
    for j in range(n):
        if i==0 and j==0:
            continue
        if i == 0:
            data[i][j] = data[i][j] + data[i][j-1]
        elif j == 0:
            data[i][j] = data[i][j] + data[i-1][j]
        else:
            data[i][j] = min(data[i-1][j],data[i][j-1]) + data[i][j]
print(data[n-1][n-1])