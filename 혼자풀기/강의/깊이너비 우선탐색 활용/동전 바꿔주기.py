t = int(input())
k = int(input())
data = [list(map(int, input().split())) for _ in range(k)]
cnt = 0
def dfs(n,s):
    if s > t:
        return
    global cnt
    if n == k:
        if s == t:
            cnt += 1
    else:
        for i in range(data[n][1]+1):
            dfs(n+1,data[n][0]*i+s)

dfs(0,0)
print(cnt)