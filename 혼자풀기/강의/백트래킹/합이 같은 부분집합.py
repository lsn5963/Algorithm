n = int (input())
data = list(map(int, input().split()))
check = [0]*(n+1)
default = False
def dfs(v):
    global default
    if v == n:

        ins = 0
        outs = 0
        for i in range(n):
            if check[i] == 1:
                ins += data[i]
            else:
                outs += data[i]

        if ins == outs:
            default = True
    else:
        check[v] = 1
        dfs(v+1)
        check[v] = 0
        dfs(v+1)
dfs(0)

if default:
    print("YES")
else:
    print("NO")