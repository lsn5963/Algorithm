from collections import deque

s,e = map(int, input().split())
visited = [False] *(10001)
def bfs(l,s):
    q = deque()
    q.append((l,s))
    visited[s] = True
    while q:
        l,tmp = q.popleft()
        if tmp == e:
            print(l)
            break

        for i in (tmp+1,tmp-1,tmp+5):
            if i >= 10001 or i <= 0:
                continue
            if visited[i] == False:
                q.append((l+1,i))
                visited[i] = True

bfs(0,s)