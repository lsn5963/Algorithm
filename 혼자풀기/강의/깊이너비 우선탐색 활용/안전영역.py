from collections import deque
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()

def bfs(i,j):
    q.append((i,j))
    visited[i][j] = 1
    dcnt = 1
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >=n or ny <0 or ny>=n:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                q.append((nx,ny))
                dcnt += 1

    return dcnt


ans = []
big,small = 0,1e9
for i in range(n):
    btmp = max(data[i])
    stmp = min(data[i])

    if btmp > big:
        big = btmp
    if stmp < small:
        small = stmp
for k in range(small, big+1):
    cnt = 0
    visited = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] < k:
                visited[i][j] = 1
    # for i in range(n):
    #     for j in range(n):
    #         print(visited[i][j], end = " ")
    #     print()
    # print("------------------------------")
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                bfs(i,j)
                cnt += 1
    ans.append(cnt)
print(max(ans))