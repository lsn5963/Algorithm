n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
rst = 0
for i in range(n):
    for j in range(n):
        x,y = i,j
        cnt = 0
        for k in range(4):
            nx,ny = x + dx[k], y + dy[k]
            if nx<0 or nx>=n or ny<0 or ny>=n:
                cnt += 1
                continue
            if data[nx][ny] < data[x][y]:
                cnt += 1

        if cnt == 4:

            rst += 1
print(rst)
