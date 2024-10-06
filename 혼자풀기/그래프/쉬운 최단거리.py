from collections import deque
q = deque()
n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            q.append((i,j))
            break
while q:
    x,y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx>= n or nx < 0 or ny>= m or ny < 0:
            continue
        if data[nx][ny] == 1:
            data[nx][ny] = data[x][y] + 1
            q.append((nx,ny))

for i in range(n):
    for j in range(m):
        if data[i][j] == 2:
            data[i][j] = 0
        elif data[i][j] == 1:
            data[i][j] = -1
        elif data[i][j] != 0:
            data[i][j] -= 2

for i in data:
    for j in i:
        print(j, end= " ")
    print()