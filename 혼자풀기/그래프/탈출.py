from collections import deque
r,c = map(int,input().split())
data = [input() for _ in range(r)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


mul = deque()
mvisited = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == '*':
            mvisited[i][j] = 1
            mul.append((i,j))
go = deque()
gvisited = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if data[i][j] == 'S':
            gvisited[i][j] = 1
            go.append((i,j))

while go:

    for _ in range(len(mul)):
        mx,my = mul.popleft()

        for i in range(4):
            nmx = mx + dx[i]
            nmy = my + dy[i]

            if nmx < 0 or nmx >= r or nmy < 0 or nmy >= c or data[nmx][nmy] == 'D' or data[nmx][nmy] == 'X' or gvisited[nmx][nmy] != 0:
                continue

            if mvisited[nmx][nmy] == 0:
                # print(mx,my,nmx,nmy)
                mvisited[nmx][nmy] = mvisited[mx][my] + 1
                mul.append((nmx,nmy))

    for _ in range(len(go)):
        gx, gy = go.popleft()

        for i in range(4):
            ngx = gx + dx[i]
            ngy = gy + dy[i]
            if ngx < 0 or ngx >= r or ngy < 0 or ngy >= c or data[ngx][ngy] == 'X' or mvisited[ngx][ngy] != 0:  # 추후 고슴도치 이동경로 필요
                continue

            if data[ngx][ngy] == "D":
                print(gvisited[gx][gy])
                exit()
            if gvisited[ngx][ngy] == 0:
                # print(mx,my,nmx,nmy)
                gvisited[ngx][ngy] = gvisited[gx][gy] + 1
                go.append((ngx, ngy))
print("KAKTUS")
