import sys
from collections import deque
n,k = map(int, sys.stdin.readline().rstrip().split())

q = deque()

for i in range(1,n+1):
    q.append(i)
print("<", end="")
while(q):
    for _ in range(k-1):
        q.append(q[0])
        q.popleft()
    print(q.popleft(), end = "")
    if q:
        print(", ", end = "")
print(">")

"""
생각은 하였지만 풀지못하였다.
구현을 많이 풀어보는 것 만이 답인것 같다.
"""