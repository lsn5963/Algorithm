n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
dp = [0]*(m+1)
for i in range(m+1):
    dp[i] = i // data[0]

for i in data:
    for j in range(i, m+1):
        if dp[j-i] + 1 < dp[j]:
            dp[j] = dp[j-i] + 1
print(dp[m])