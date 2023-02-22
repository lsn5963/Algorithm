n,m = map(int, input().split())

def DFS(v):
    global cnt

    if m == v:
        for i in range(m):
            if res[i] != 0:
                print(res[i], end = " ")
        cnt += 1
        print()
    else:
        for i in range(n):
            res[v] = i+1
            DFS(v+1)
res = [0] *(m)    
cnt = 0
DFS(0)
print(cnt)