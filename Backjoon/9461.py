import sys
n = int(sys.stdin.readline().rstrip())

data = []
dp = [0] * 101
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
for i in range(6,101):
    dp[i] = dp[i-5] + dp[i-1]
for i in data:
    print(dp[i])

"""
역시 점화식을 찾아 풀었다!
다른 풀이를 보면 점화식이 다르지만 결과는 같게 나온다.
"""
