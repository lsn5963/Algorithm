from itertools import count
import sys
from collections import deque
n,m,r = map(int,sys.stdin.readline().rstrip().split())
visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]
cnt = 1
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def bfs(r):
    global cnt

    q = deque([r])
    visited[r] = 1

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                cnt +=1
                visited[i] = cnt
                q.append(i)
bfs(r)