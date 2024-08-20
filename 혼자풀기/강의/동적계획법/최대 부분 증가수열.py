n = int(input())
data = list(map(int, input().split()))

dp = [0]*n
dp[0] = 1
for i in range(1,n):
    m = 0
    for j in range(i-1,-1,-1):
        if data[i] > data[j]:
            if dp[j] > m:
                m = dp[j]
    dp[i] = m + 1
print(max(dp))