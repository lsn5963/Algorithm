n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0

def dfs(x,y):
    global cnt
    if x == bn[0] and y == bn[1]:
        cnt += 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        # if visited[nx][ny] == 1:
        #     continue
        if data[x+dx[i]][y+dy[i]] > data[x][y]:
            # visited[x+dx[i]][y+dy[i]] = 1
            dfs(x+dx[i],y+dy[i])
            # visited[x+dx[i]][y+dy[i]] = 0
s = 1e9
b = 0
sn = 0
bn = 0
for i in range(n):
    for j in range(n):
        if data[i][j] > b:
            b = data[i][j]
            bn = (i,j)
        if data[i][j] < s:
            s = data[i][j]
            sn = (i, j)
visited[sn[0]][sn[1]] = 1
dfs(sn[0],sn[1])
print(cnt)