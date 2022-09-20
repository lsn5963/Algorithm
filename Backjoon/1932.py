import sys
n = int(sys.stdin.readline().rstrip())

data = []
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))


k = 2
for i in range(1, n):
    for j in range(k):
        if j == 0:
            data[i][0] += data[i-1][0]
        elif i == j:
            data[i][j] += data[i-1][j-1]
        else:
            data[i][j] += max(data[i-1][j-1],data[i-1][j])
    k += 1
print(max(data[n-1]))

"""
답지를 보고 풀었다.
좀 더 생각해보고 풀어야겠다
"""