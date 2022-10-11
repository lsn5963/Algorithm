from collections import deque
import sys

n,k = map(int, sys.stdin.readline().rstrip().split())

visited = [0 for _ in range(100001)] # == [0]*(100001)

def bfs():
    q = deque()
    q.append(n)
    
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)
bfs()
# 5 - 1  1

# 2*4    1

# 2*8    1

# 16 + 1 1

"""
이런 유형은 또 오랜만에 본 것 같다.
유형에 빨리 익숙해져야겠다.
"""