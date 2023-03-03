n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
# data.insert(0,[0,0])
res = []
def DFS(v,sum):
    if v == n:
        res.append(sum)
        return
    else:
        if data[v][0]+v<= n:
            DFS(data[v][0]+v,sum + data[v][1])
        DFS(v+1,sum)
sum = 0
ch = 0
DFS(0,sum)
print(max(res))