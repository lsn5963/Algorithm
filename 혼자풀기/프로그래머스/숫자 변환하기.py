from collections import deque
def solution(x, y, n):
    visited = [0]*(y+1)
    q = deque()
    q.append((x,0))
    while q:
        x,cnt = q.popleft()
        if x == y:
            return cnt
        for i in (x+n,x*2,x*3):
            if i <= y and visited[i] == 0 :
                visited[i] = cnt+1
                q.append((i,cnt+1))
    return -1
print(solution(10,40,5))