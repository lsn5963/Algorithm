from collections import deque
s,e = map(int, input().split())

q = deque()
q.append((s,0))
visited = [False]*(10001)
while True:
    x,cnt = q.popleft()
    if x == e:
        print(cnt)
        break
    for i in x+1, x-1, x+5:
        if i<0 or i > 10000:
            continue
        # if i > e+1:
        #     break
        # print(i)
        if visited[i] == False:
            q.append((i,cnt + 1))
            visited[i] = True