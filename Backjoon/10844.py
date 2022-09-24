import sys

n = int(sys.stdin.readline().rstrip())

data = [[0]*10 for _ in range(n+1)]

for i in range(1,10):
    data[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            data[i][0] = data[i-1][1]
        elif j == 9:
            data[i][9] = data[i-1][8]
        else:
            data[i][j] = data[i-1][j-1] + data[i-1][j+1]
print(sum(data[n])%1000000000)

"""
답지를 보고 풀었다.
수학문제를 푸는 것만 같다.
아직 익숙하지 않은 것 같다.
"""