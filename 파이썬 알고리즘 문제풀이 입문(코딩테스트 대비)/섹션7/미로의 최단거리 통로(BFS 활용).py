from collections import deque
data = [list(map(int, input().split())) for _ in range(7)]

#상하좌우
dx = [0,0,-1,1] 
dy = [-1,1,0,0]

tmp = [[0]* 7 for _ in range(7)]


dq = deque()
dq.append([0,0])
while dq:
    x,y = dq.popleft()
    data[x][y] = 1
    if x ==6 and y == 6:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx<=-1 or nx >=7 or ny<=-1 or ny >=7:
            continue
        
        if data[nx][ny] == 1:
            continue

        tmp[nx][ny] = tmp[x][y] + 1
        dq.append([nx,ny])
if tmp[6][6] == 0:
    print(-1)
else:
    print(tmp[6][6])