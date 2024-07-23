from collections import deque
n,m = map(int, input().split())
data = list(map(int, input().split()))

q = deque()
cnt = 0
for i in range(n):
    q.append((data[i],i))
while q:
    # print(q)
    num,idx = q[0][0],q[0][1]
    for i in range(1,len(q)):
        if num<q[i][0]:
            q.append(q.popleft())
            break
    else:
        t,id = q.popleft()
        cnt += 1
        if id ==m:
            print(cnt)
            break
