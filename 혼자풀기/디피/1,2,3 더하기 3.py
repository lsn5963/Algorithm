t = int(input())
data = [int(input()) for _ in range(t)]
n = max(data)
dp = [0]*(n+1)
dp[0] = 1
dp[1] = 2
dp[2] = 4
for i in range(3,n):
    dp[i] = (dp[i-3]+dp[i-2]+dp[i-1])%1000000009
for i in data:
    print(dp[i-1])