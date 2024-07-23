from collections import deque
seq = list(input())
n = int(input())
data = []
for i in range(n):
    tmp = input()
    dq = deque(seq)
    for j in tmp:
        if j in seq:
            if j != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) != 0:
            print("#%d NO" %(i+1))
        else:
            print("#%d YES" %(i+1))

