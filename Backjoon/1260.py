import imp
import sys
from collections import deque
n,m,v = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    global cnt
    visited[v] = cnt
    print(v, end = " ")
    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            dfs(i)
def bfs(v):
    global cnt
    q = deque([v])
    visited[v] = 1
    while q:
        t = q.popleft()
        print(t, end = " ")
        for i in graph[t]:
            if visited[i] == 0:
                cnt += 1
                visited[i] = cnt
                q.append(i)       
dfs(v)
cnt = 1
visited = [0] * (n+1)
print()
bfs(v)

"""
비슷한 개념들의 반복인 것 같다.
"""