import sys

k = int(sys.stdin.readline().rstrip())

data = []

for _ in range(k):
    t = int(sys.stdin.readline().rstrip())
    if t == 0:
        data.pop()
    else:
        data.append(t)

print(sum(data))

"""
쉬운문제였다.
스택에 대해 다시공부하게 해주는 좋은 문제다!
"""
