n = int(input())
data = list(map(int, input().split()))

dp = [1]*(1001)
dp[0] = 1

for i in range(n):
    for j in range(i-1,-1,-1):
        if data[i] < data[j]:
            # print(i,j)
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))