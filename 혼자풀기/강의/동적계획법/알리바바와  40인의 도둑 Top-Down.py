from collections import deque
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
dx = [0,1]
dy = [1,0]
q = deque()
q.append((0,0))
dp = [[0]*n for _ in range(n)]

def dfs(x,y):
    if dp[x][y] > 0:
        return dp[x][y]
    if x==0 and y==0:
        return data[0][0]
    elif x == 0:
        dp[x][y] = dfs(x,y-1) + data[x][y]
    elif y == 0:
        dp[x][y] = dfs(x-1, y) + data[x][y]
    else:
        dp[x][y] = min(dfs(x,y-1),dfs(x-1,y)) + data[x][y]
    return dp[x][y]
print(dfs(n-1,n-1))
