n, m = map(int, input().split())
def dfs(v,l):
    global cnt
    if v == m:
        for i in res:
            print(i, end = " ")

        print()
        cnt += 1
    else:
        for i in range(l,n+1):
            # if ch[i] == 0:
                # ch[v] = 1
            # if v < i:
            res[v] = i
            dfs(v+1,i+1)


# ch = [0] * (n)
res = [0] * (m)
cnt = 0
dfs(0,1)
print(cnt)