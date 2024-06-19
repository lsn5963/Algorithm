from collections import deque
n = int(input())
f,d = map(int,input().split())
m = int(input())
data = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

visited = [ False for _ in range(n+1)]

q = deque()
q.append((f,0))

while q:
    tmp, cnt = q.popleft()
    if tmp == d:
        print(cnt)
        exit()
    for i in data[tmp]:
        if visited[i] == False:
            visited[i] = True
            q.append((i,cnt + 1))
print(-1)