n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort(key = lambda x: x[0], reverse = True)

dp = [0]*(n)
dp[0] = data[0][1]

for i in range(1,n):
    m = data[i][1]
    for j in range(i-1,-1,-1):
        if data[i][2] < data[j][2]:
            if dp[j]+data[i][1] > m:
                m = dp[j] + data[i][1]
    dp[i] = m
print(max(dp))
