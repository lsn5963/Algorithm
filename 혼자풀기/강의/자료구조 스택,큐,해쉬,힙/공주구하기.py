from collections import deque
n,k = map(int, input().split())
q = deque(list(range(1,n+1)))
rst = []
while q:
    # print(q)
    for i in range(k-1):
        q.append(q.popleft())
    q.popleft()

    if len(q) == 1:
        print(q[0])
        break
