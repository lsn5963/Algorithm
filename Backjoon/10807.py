import sys

n = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))

v = int(sys.stdin.readline().rstrip())

print(data.count(v))