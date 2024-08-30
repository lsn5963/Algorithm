n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
ans = 0
# def dfs(num,s,t):
#     global ans
#     if t>m:
#         return
#     if num == n:
#         ans = max(ans,s)
#     else:
#         dfs(num+1,s+data[num][0],t+data[num][1])
#         dfs(num+1, s, t)
# dfs(0,0,0)
# print(ans)

dp = [0]*(m+1)
for i in data:
    for j in range(m,i[1]-1,-1):
        # print(j)
        if dp[j-i[1]] + i[0] > dp[j]:
            dp[j] = dp[j-i[1]] + i[0]
print(max(dp))