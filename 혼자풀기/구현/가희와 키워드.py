import sys
n,m = map(int,sys.stdin.readline().split())
memo = [sys.stdin.readline().rstrip() for _ in range(n)]
data = {}
for i in memo:
    data[i] = 1
cnt = n
for _ in range(m):
    post = sys.stdin.readline().rstrip().split(",")
    for i in post:
        if i in data:
            if data[i] == 1:
                data[i] -= 1
                cnt -= 1
    print(cnt)