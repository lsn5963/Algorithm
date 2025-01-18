n = int(input())
data = list(map(int,input().split()))
dp = [0]*(n+1)
dp[0] = data[0]
s = 0
for i in range(1,n):
    if dp[i-1]+data[i]>data[i]:
        dp[i] = dp[i-1]+data[i]
    else:
        dp[i] = data[i]
print(dp)