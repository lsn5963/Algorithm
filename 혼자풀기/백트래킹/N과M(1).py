n,m = map(int, input().split())
visited = [False] *(n+1)
rst = [0] *(m+1)
def dfs(v):
    if v == m+1:
        for i in range(1,m+1):
            print(rst[i], end= " ")
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == False:
                visited[i] = True
                rst[v] = i
                dfs(v+1)
                visited[i] = False
dfs(1)