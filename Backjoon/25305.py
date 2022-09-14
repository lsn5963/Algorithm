import sys
n, k = map(int, sys.stdin.readline().rstrip().split())

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort(reverse=True)
print(data[k-1])

"""
쉽다.
"""