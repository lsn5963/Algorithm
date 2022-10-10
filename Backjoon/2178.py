import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]



graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))


def bfs(x,y):
    q= deque([(x,y)])
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx,ny])

    return graph[n-1][m-1]
print(bfs(0,0))


"""
또 이런 유형은 첨이라서 답을 보고 했다.
하지만 bfs는 비슷한 코드에서 조금만 바꾸면 되는것같기에 많이 풀다보면 익숙해질 것 같다.
"""