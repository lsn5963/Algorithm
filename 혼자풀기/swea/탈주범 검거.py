from collections import deque
t = int(input())
dx = [[-1,1,0,0],[-1,1],[0,0],[-1,0],[1,0],[1,0],[-1,0]]
dy = [[0,0,-1,1],[0,0],[-1,1],[0,1],[0,1],[0,-1],[0,-1]]
no = {
    (-1,0) : [3,4,7],
    (1,0) : [3,5,6],
    (0,-1) : [2,6,7],
    (0,1) : [2,4,5]
}
for tt in range(t):
    n,m,r,c,l = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(n)]

    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((r,c)) # 시작점 넣기
    visited[r][c] = 1

    while q:
        x,y = q.popleft()
        pipe = data[x][y] #3
        if visited[x][y] == l:
            continue
        move = len(dx[pipe-1]) # 파이프가 빠져나갈 수 있는 통로의 갯수
        for i in range(move):


            nx = x + dx[pipe-1][i]
            ny = y + dy[pipe-1][i]
            if nx>= 0 and nx<n and ny>=0 and ny<m and visited[nx][ny] == 0 and data[nx][ny] !=0:
                chx = dx[pipe - 1][i]
                chy = dy[pipe - 1][i]
                # print(data[nx][ny])
                # print(chx)
                # print(chy)
                if data[nx][ny] not in no[(chx,chy)]:
                    q.append((nx,ny))
                    visited[nx][ny] = visited[x][y] + 1

    cnt = 0
    for i in visited:
        for j in i:
            if j != 0:
                cnt += 1
    print("#", end = "")
    print(tt+1,cnt)