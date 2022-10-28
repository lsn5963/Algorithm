import sys

n, m =map(int, sys.stdin.readline().rstrip().split())
data = []
for i in range(n+n):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))

rst = []
for i in range(n):
    for j in range(m):
        print(data[i][j]+data[i+n][j], end=" ")

    print()

