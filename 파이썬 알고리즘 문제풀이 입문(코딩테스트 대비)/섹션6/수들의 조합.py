n,k = map(int, input().split())
data = list(map(int, input().split()))
m = int(input())

def DFS(v,s):
    global cnt
    if v == k:
        if sum(res) % m == 0:
            cnt += 1
    else:
        for i in range(s,n):
            # print(v)
            res[v] = data[i]
            DFS(v+1,i+1)
res = [0] * k
cnt = 0
DFS(0,0)
print(cnt)