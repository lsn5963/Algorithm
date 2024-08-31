n = int(input())
data = [[5000]*(n+1) for _ in range(n+1)]
for i in range(n+1):
    data[i][i] = 0
a,b = 0,0
while a != -1 and b != -1 :
    a,b = map(int,input().split())
    data[a][b] = 1
    data[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            data[i][j] = min(data[i][j],data[i][k]+data[k][j])

ans = [0]*(n+1)

for i in range(1,n+1):
    for j in range(1,n+1):
        if data[i][j] == 5000:
            data[i][j] = 0
            continue
        else:
            ans[j] = max(ans[j],data[i][j])
print(min(ans[1:]),ans.count(min(ans[1:])))
for i in range(1,n+1):
    if ans[i] == min(ans[1:]):
        print(i, end = " ")



