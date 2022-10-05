import sys
n = int(sys.stdin.readline().rstrip())

data = list(map(int, sys.stdin.readline().rstrip().split()))
cnt = 0
for i in range(n):
    if i == n-2:
        if data[i+1] - data[i] > 0:
            cnt +=1

        break
    if data[i+1] - data[i] > 0:
        cnt +=1
if data[1] - data[0] > 0:
        cnt +=1
print(cnt)