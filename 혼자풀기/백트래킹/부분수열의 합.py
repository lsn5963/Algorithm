n,s = map(int, input().split())
data = list(map(int, input().split()))
cnt = 0
visited = [False] *(n)
def dfs(v):
    global cnt
    if v == n:
        rst = 0
        check = 0
        for i in range(n):
            if visited[i] == True:
                rst += data[i]
            else:
                check += 1

        if rst == s:
            if check == n:
                return
            else:
                cnt += 1
    else:
        visited[v] = True
        dfs(v+1)
        visited[v] = False
        dfs(v+1)
dfs(0)
print(cnt)