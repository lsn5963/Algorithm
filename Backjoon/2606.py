import sys
from collections import deque
cpn = int(sys.stdin.readline().rstrip())
netn = int(sys.stdin.readline().rstrip())
visited = [0] * (cpn + 1)
cnt = 1

graph = [[] for _ in range(cpn+1)]

for _ in range(1, netn+1):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

visited[1] = cnt
while(q):
    v = q.popleft()
    
    for i in graph[v]:
        if visited[i] == 0:
            cnt+=1
            visited[i] = cnt
            q.append(i)
print(max(visited)-1)

"""
오랜만에 혼자서 푼 문제이다.
솔직히 말하면 왜풀린지 모르겠다.
dfs/bfs를 언제 적용해야하는지 모르겠다.
다시 공부해봐야겠다.
"""