import sys

n = int(sys.stdin.readline())
#1 pop(1)
#2 lt,rt
import heapq
q = []
#4 deque
data = []
for i in range(n):
    s = int(sys.stdin.readline())
    if s == 0:
        if q == []:
            print(0)
            continue
        print(heapq.heappop(q))
        continue
    heapq.heappush(q,s)
