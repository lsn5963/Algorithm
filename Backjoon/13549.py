import sys
from collections import deque

n,k = map(int, sys.stdin.readline().rstrip().split())

visited = [-1] * 100001 # == [0]*(100001)

def bfs():
    q = deque()
    q.append(n)
    visited[n] = 0
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        for nx in (x+1, x-1, x*2):
            if 0 <= nx < 100001 and visited[nx] == -1:
                if nx == x*2:
                    visited[nx] = visited[x]
                    q.appendleft(nx)
                else:
                    visited[nx] = visited[x] + 1
                    q.append(nx)
bfs()

"""
이런 유형은 또 오랜만에 본 것 같다.
유형에 빨리 익숙해져야겠다.

전에 풀었던 문제와 거의 똑같은 유형이다.
왜 x*2일 때 q.appendleft를 해주는지 정확히 이해가 가지 않는다.
https://www.acmicpc.net/board/view/73660
"""