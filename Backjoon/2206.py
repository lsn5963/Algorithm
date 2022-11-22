from collections import deque
import sys

n,m = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    data.append(list(map(int,(sys.stdin.readline().rstrip()))))

dx = [1,-1,0,0] #상하좌우
dy = [0,0,-1,1]

q = deque()
q.append([0,0])
def bfs():

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if data[nx][ny] == 0:
                data[nx][ny] = data[x][y] + 1
                q.append([nx,ny])

bfs()
print(data)