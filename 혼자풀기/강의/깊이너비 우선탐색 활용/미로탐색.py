data = [list(map(int,input().split())) for _ in range(7)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
cnt = 0
def dfs(x,y):
    global cnt
    if x<0 or x>=7 or y<0 or y>=7:
        return
    if data[x][y] == 1:
        return
    if x == 6 and y == 6:
        cnt += 1
        return
    for i in range(4):
        data[x][y] = 1
        dfs(x+dx[i],y+dy[i])
        data[x][y] = 0
dfs(0,0)
print(cnt)