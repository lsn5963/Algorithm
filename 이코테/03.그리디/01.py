import sys

n = sys.stdin.readline().rstrip()

data = list(map(int, sys.stdin.readline().rstrip().split()))
data.sort()
count = 0
gr = 0
for i in data:
    count += 1
    if count == i:
        gr += 1
        count = 0
print(gr)


"""
이문제는 이 방식으로 접근하기 어려웠다.
다음에 다시풀어봐야할 문제이다.
"""