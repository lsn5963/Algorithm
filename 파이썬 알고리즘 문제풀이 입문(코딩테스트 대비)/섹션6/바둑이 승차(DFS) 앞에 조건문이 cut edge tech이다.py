c, n = map(int, input().split())
def DFS(v, sum,tsum):
    global m
    if sum + (total-tsum) < m:
        return
    if sum > c:
        return

    if v == n:
        rst.append(sum)
        m = max(rst)
    else:
        DFS(v+1,data[v]+sum,data[v]+tsum)
        DFS(v+1,sum,data[v]+tsum)

data = [int(input()) for _ in range(n)]
rst = []
total = sum(data)
m = 0
DFS(0,0,0)
print(max(rst))