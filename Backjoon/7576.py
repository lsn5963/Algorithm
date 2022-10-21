from collections import deque
import sys
m,n = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

q = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():

    while q:

        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            # if graph[nx][ny] == -1:
            #     continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])
        
cnt = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i,j])
# q.append([,0])
        
bfs()   
result = 0  
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit()
        result = max(result, j)
print(result-1)

"""
무언가 계속 비슷한 문제가 나오지만 생각을 해내지 못한다.
bfs를 구현할 수 있는데 왜 응용이 될 때마다 아이디어가 떠오르지 않는지 모르겠다 ㅠㅠ
많이 노력해야겠다.
"""