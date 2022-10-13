from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())

dx = [1,2,2,1,-1,-2,-2,-1] #시계 방향
dy = [-2,-1,1,2,2,1,-1,-2]
def bfs(a,b):
    q = deque()
    q.append([a,b])
    visited[a][b] = 1
    while q:
        x,y = q.popleft()
        if x == c and y == d:
            print(visited[x][y]-1)
            break
        for i in range(8):
            nx = x +dx[i] 
            ny = y +dy[i]

            if nx<0 or nx>=l or ny<0 or ny>=l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
              
for _ in range(n):
    l = int(sys.stdin.readline().rstrip())
    a,b = map(int, sys.stdin.readline().rstrip().split())
    c,d = map(int, sys.stdin.readline().rstrip().split())

    visited = [[0]*l for _ in range(l)]
    bfs(a,b)

"""
변수때문에 시간을 너무 많이 잡아먹었다.
그래도 다 비슷한 유형이라 할만하다.
"""