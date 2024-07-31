n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
rst = 0
tot = sum(a for a,b in data)
def dfs(num,s,t,tsum):
    global rst
    if tot - tsum + s < rst:
        return
    if t > m:
        return
    if n == num:
        rst = max(rst,s)
    else:
        dfs(num + 1,s + data[num][0],t+data[num][1],tsum+data[num][0])
        dfs(num + 1, s, t, tsum + data[num][0])
dfs(0,0,0,0)
print(rst)