n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]
print(data)
ans = 0
sum = 0
time = 0
def dfs(v,sum,time):
    global ans
    if time > m:
        return
    if v == n:
        ans = max(ans,sum)
        return
    dfs(v+1,sum+data[v][0],time+data[v][1])
    dfs(v+1,sum,time)

dfs(0,sum,time)
print(ans)