from collections import deque
n, m = map(int, input().split())

ch = [0] * (100001)
dis = [0] * (100001)

ch[n] = 1

dq = deque()
dq.append(n)

while dq:
    now = dq.popleft()
    if now == m:
        break
    for next in(now-1, now+1, now+5):
        if 0< next < 10001:
            if ch[next] ==0:
                dq.append(next)
                ch[next] = 1
                dis[next] = dis[now] + 1

print(dis[m])