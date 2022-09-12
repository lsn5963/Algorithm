import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())

q = deque()
for i in range(1,n+1):
    q.append(i)

while(True):
    if len(q) == 1:
        break
    q.popleft()
    
    temp = q.popleft()
    q.append(temp)
print(q[0])


"""
이문제는 입력값 1을 생각하지 못하고 풀었다.
아쉬운 문제다
"""