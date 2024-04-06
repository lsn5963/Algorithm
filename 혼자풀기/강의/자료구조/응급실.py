from collections import deque
n,m = map(int, input().split())
data = list(map(int, input().split()))
q  = deque(data)

ch = [False] *(n)
ch[m] = True
ch = deque(ch)
cnt = 1

while q:
    # print(q)
    # print(ch)
    tmp = q.popleft()
    chtmp = ch.popleft()

    for i in q:
        if i > tmp:
            q.append(tmp)
            ch.append(chtmp)
            break
    else:
        if chtmp == True:
            break
        else:
            cnt += 1
print(cnt)