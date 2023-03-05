t = int(input())
k = int(input())
data = [list(map(int, input().split())) for _ in range(k)]
rst = []
cnt = 0

def dfs(i,sum):
    global cnt
    if i == k:
        if sum == t:
            cnt += 1
        return
    if sum > t:
        return
    else:
        for j in range(data[i][1]+1):
            dfs(i+1,sum+data[i][0]*j)
dfs(0,0)
print(cnt)
