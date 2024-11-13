from collections import deque
n = int(input())
data = [list(input()) for _ in range(n)]

q = deque()
q.append((0,0))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for _ in range(n)]
def bfs(x,y):
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>= n or ny < 0 or ny >=n:
                continue

            if data[x][y] != data[nx][ny]:
                continue
            if visited[nx][ny] == True:
                continue
            q.append((nx,ny))
            visited[nx][ny] = True

cnt = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            q.append((i, j))
            bfs(i,j)
            cnt += 1
print(cnt, end = " ")
visited = [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if data[i][j] == "G":
            data[i][j] = "R"
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            visited[i][j] = True
            q.append((i, j))
            bfs(i,j)
            cnt += 1
print(cnt)