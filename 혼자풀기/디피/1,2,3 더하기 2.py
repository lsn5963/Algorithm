n,k = map(int, input().split())
data = [1,2,3]
rst = []
def dfs(s,m):
    if s == n:
       rst.append(m)
    if s > n:
        return
    else:
        for i in range(3):
            dfs(s+data[i],m+"+"+str(data[i]))
dfs(0,"")
if len(rst)< k:
    print(-1)
else:
    print(rst[k-1][1:])