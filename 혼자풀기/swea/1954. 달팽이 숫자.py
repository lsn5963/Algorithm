t = int(input())
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for k in range(1,t+1):
    n = int(input())
    cnt = 1
    d = 0
    check = [[0]*n for _ in range(n)]
    x,y = 0,0
    print("#",end="")
    print(k)
    for i in range(n*n):
        check[x][y] = cnt
        nx = x + dx[d]
        ny = y + dy[d]
        cnt += 1
        if nx >= 0 and nx < n and ny >= 0 and ny < n and check[nx][ny] == 0:
            x,y = nx,ny
            # check[x][y] = cnt
        else:
            d = (d+1)%4
            x = x + dx[d]
            y = y + dy[d]
            # check[x][y] = cnt

    for i in range(n):
        for j in range(n):
            print(check[i][j], end = " ")
        print()
