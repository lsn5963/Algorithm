import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

data = []
result = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().rstrip())))

dx = [-1,1,0,0] # 상하좌우
dy = [0,0,-1,1]

def bfs(a,b):
    q = deque()
    q.append([a,b])
    data[a][b] = 0  # 방문처리
    cnt = 1

    while q:
        x,y = q.popleft()
        data[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>= n or ny<0 or ny>=n:
                continue
            if data[nx][ny] == 1:
                data[nx][ny] = 0
                cnt+=1
                q.append([nx,ny])
    return cnt

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            result.append(bfs(i,j))
print(len(result))
result.sort()
for i in result:
    print(i)

"""
이런 유형은 처음이라 많이 어려웠다.
답지를 보고 풀었지만 익숙해진다면 충분히 풀 수 있을 것 같다.
"""