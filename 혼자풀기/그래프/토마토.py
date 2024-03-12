from collections import deque
m,n = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            q.append((i,j))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
    x,y = q.popleft()


    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<0 or nx >= n or ny <0 or ny >=m:
            continue

        if data[nx][ny] == 0:
            data[nx][ny] = data[x][y] + 1
            q.append((nx,ny))
success = True
rst = 0
for da in data:
    for j in da:
        if j == 0:
            success = False
        rst = max(rst,j)

if success == False:
    print(-1)
else:
    print(rst-1)

