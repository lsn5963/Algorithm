import sys

n = int(sys.stdin.readline().rstrip())
data = [0] * 10000
for i in range(n):
    data[i] = (int(sys.stdin.readline().rstrip()))

dp = [0] * 10000

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(dp[1], data[0]+data[2], data[1]+data[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+data[i], dp[i-1], dp[i-3]+data[i-1]+data[i])
print(max(dp))

"""

답을 보고 풀었지만 무언가 감이 잡히는 느낌이다.

"""