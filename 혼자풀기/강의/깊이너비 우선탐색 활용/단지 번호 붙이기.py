from collections import deque
n = int(input())
data = [list(map(int,input().rstrip())) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
q = deque()

def bfs(i,j):
    q.append((i,j))
    data[i][j] = 0
    dcnt = 1
    while q:
        x,y = q.popleft()
        # print(x,y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx >=n or ny <0 or ny>=n:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                q.append((nx,ny))
                dcnt += 1

    return dcnt


cnt = 0
ans = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            cnt += 1
            ans.append(bfs(i,j))
ans.sort()
print(cnt)
for i in range(len(ans)):
    print(ans[i])