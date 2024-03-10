n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
ans = 0
t,p = 0,0
def dfs(v,p):
    global ans
    if v >= n:
        ans = max(ans,p)
        return
    else:
        if v+data[v][0] <= n:
            dfs(v+data[v][0],p+data[v][1])
        dfs(v+1,p)

dfs(0,p)
print(ans)