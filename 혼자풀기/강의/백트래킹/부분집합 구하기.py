n = int(input())
visited = [False] *(n+1)
def dfs(v):
    if v == n+1:
        for i in range(1, n+1):
            if visited[i] == True:
                print(i, end = " ")
        print()
    else:
        visited[v] = True
        dfs(v+1)
        visited[v] = False
        dfs(v+1)


dfs(1)