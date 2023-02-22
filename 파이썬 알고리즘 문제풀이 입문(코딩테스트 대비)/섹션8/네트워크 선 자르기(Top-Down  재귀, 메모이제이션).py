n = int(input())

def func(v):
    if v == 1:
        return 1
    if v == 2:
        return 2
    if dp[v] != 0:
        return dp[v]
    else:
        dp[v] = func(v-2) + func(v-1)
dp = [0] *(n+1)

func(n)
print(dp[n])
