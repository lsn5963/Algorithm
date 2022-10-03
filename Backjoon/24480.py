import sys
sys.setrecursionlimit(10**6)
cnt = 1
def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt

    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            dfs(graph, i, visited)

n,m,r = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

dfs(graph, r, visited)

for i in visited[1:]:
    print(i)

"""
rever = True를 왜 생각못했을까.
다음에는 생각해봐야겠다.
"""