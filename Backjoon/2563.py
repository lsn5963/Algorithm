import sys

n = int(sys.stdin.readline().rstrip())
data = [[0 for i in range(101)]for _ in range(101)]
for i in range(n):
    x,y = map(int, sys.stdin.readline().rstrip().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            data[i][j] = 1
count = 0
for i in data:
    count += i.count(1)

print(count)