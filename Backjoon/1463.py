import sys

n = int(sys.stdin.readline().rstrip())

dp = [0] *(n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
print(dp[n])

"""
담에는 절대 답을 보고 풀지 말아야겠다.
"""