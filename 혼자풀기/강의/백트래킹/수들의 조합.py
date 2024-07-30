n,k = map(int, input().split())
data = list(map(int, input().split()))
m = int(input())

cnt = 0
def dfs(l,s,c):
    global cnt
    if l == n:
        if c == k:
            if s % m == 0:
                cnt += 1
        return
    dfs(l+1,s+data[l],c+1)
    dfs(l + 1, s, c)
dfs(0,0,0)
print(cnt)

