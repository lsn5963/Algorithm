n,m = map(int,input().split())

a,b,d = map(int,input().split())
x,y = a,b
data = [list(map(int,input().split())) for _ in range(n)]
tmp = 0
if data[x][y] == 1:
    cnt = 0
else:
    cnt = 1
while True:
    if tmp == 4:
        if d == 0:
            nx,ny = x+1,y
        elif d == 1:
            nx,ny = x,y-1
        elif d == 2:
            nx,ny = x-1,y
        else:
            nx,ny = x,y+1

        if nx > b or nx < 0 or ny > a or ny < 0 or data[nx][ny] == 1:
            break
        else:
            tmp = 0

    if d == 0:  # 북쪽
        nx,ny = x,y-1
        d = 3 # 서쪽
    elif d == 1: # 동쪽
        nx,ny = x-1,y
        d = 0 # 북쪽
    elif d == 2: # 남쪽
        nx,ny = x,y+1
        d = 1 # 동쪽
    else:   # 서쪽
        nx,ny = x+1,y
        d = 2 # 남쪽

    tmp += 1
    if nx > b or nx < 0 or ny > a or ny < 0:
        continue # 범위 벗어남
    if data[nx][ny] == 1:
        continue # 바다 or 가본 칸

    # 정상+
    tmp = 0
    x,y = nx,ny
    cnt += 1
    data[nx][ny] = 1
print(cnt)