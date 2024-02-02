c,n = map(int, input().split())
data = [int(input()) for _ in range(n)]
visited = [0] * (n)
m = 0
total = sum(data)
def dfs(v,sum,tsum):
    global m
    if sum+total-tsum < m:
        return
    if sum > c:
        return
    if v == n:
        if m < sum:
            m = sum
    else:
        dfs(v+1,sum+data[v],tsum+data[v])
        dfs(v+1,sum,tsum+data[v])
dfs(0,0,0)
print(m)