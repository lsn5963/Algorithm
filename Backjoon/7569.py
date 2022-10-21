from collections import deque
import sys

m,n,h = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(h)]
for i in range(h):
    for j in range(n):
        graph[i].append((list(map(int, sys.stdin.readline().rstrip().split()))))



dx = [0,0,-1,1,0,0] # 위 아래 왼쪽 오른쪽 앞 뒤
dy = [0,0,0,0,-1,1]
dz = [1,-1,0,0,0,0]
q= deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if graph[z][y][x] == 1:
                q.append([x,y,z]) 
def bfs():
    while q:

        x,y,z = q.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx<0 or nx>=m or ny<0 or ny>=n or nz<0 or nz>=h:
                continue
            if graph[nz][ny][nx] == 0:
                graph[nz][ny][nx] = graph[z][y][x] + 1
                q.append([nx,ny,nz])

    
bfs()
t = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
            t = max(t, k)


print(t-1)

"""
저번 토마토문제와 거의 같은 문제이다
2차원에서 3차원으로 바뀐 것 인데 차원을 다루는게 어려웠다.
차원을 다룰 수 있었던 좋은 문제다.
"""