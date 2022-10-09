from collections import deque
import sys

t = int(sys.stdin.readline().rstrip())

dx = [-1,1,0,0] #상하좌우
dy = [0,0,-1,1]


def bfs(i,j):
    q = deque()
    q.append([i,j])
    graph[i][j] = 0 #방문처리

    while q:
        x,y = q.popleft()
        graph[x][y] = 0 # 방문처리

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append([nx,ny])
result = []
for k in range(t):
    
    m,n,k = map(int, sys.stdin.readline().rstrip().split())

    graph = [[0]*m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        a,b = map(int, sys.stdin.readline().rstrip().split())

        graph[b][a] = 1

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                result.append(bfs(i,j))
                cnt+=1
    print(cnt)
"""
2667번과 거의 비슷한 문제라서 거의 풀었다.
디테일 부분을 잘 해결하지 못해 아쉬웠다.
좀만 더 한다면 완벽하게 풀것같다.
"""