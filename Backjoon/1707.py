import sys
from collections import deque
k = int(sys.stdin.readline().rstrip())

def bfs(start):
    visited[start] = 1
    queue = deque()
    queue.append(start)

    while queue:
        x = queue.popleft()
        for i in data[x]:

            if not visited[i]:
                queue.append(i)
                visited[i] = -visited[x]
            elif visited[i] == visited[x]:
                return False
    return True

for i in range(k):
    v,e = map(int,sys.stdin.readline().rstrip().split())
    data = [[] for _ in range(v+1)]
    visited = [False] * (v+1)

    for j in range(e):
        a, b = map(int,sys.stdin.readline().rstrip().split())
        data[a].append(b)
        data[b].append(a)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i) 
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")
