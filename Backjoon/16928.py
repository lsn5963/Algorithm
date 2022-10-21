from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
game = [i for i in range(101)]
visited = [0] *(101)
ladder = []
for _ in range(n+m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    game[a] = b


q = deque()
def bfs():
    q.append(1)
    visited[1] = 1
    while q:
        t = q.popleft()
        for i in range(1,7):
            temp = i + t

            if temp > 100:
                break
            cnt = game[temp]

            if visited[cnt] == 0:
                q.append(cnt)
                visited[cnt] = visited[t] + 1

                if cnt == 100:
                    return
bfs()
print(visited[100]-1)
            
            
"""
이문제를 왜 2차원으로 접근했는지 모르겠다.
쉽게 생각하면 쉽게 풀 수 있는 문제인데 아쉽다.
"""