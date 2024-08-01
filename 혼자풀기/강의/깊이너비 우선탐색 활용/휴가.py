n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
rst = 0
def dfs(num,t,p):
    global rst
    if num > n:
        return
    if num == n:
        rst = max(rst,p)
    else:
        dfs(num+data[num][0],t+data[num][0],p+data[num][1])
        dfs(num + 1, t, p)

dfs(0,0,0)
print(rst)