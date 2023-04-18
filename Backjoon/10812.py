n, m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(m)]
rst = list(range(1,n+1))
for i,j,k in data:
    rst = rst[:i-1]+rst[k-1:j] + rst[i-1:k-1] + rst[j:]

for i in rst:
    print(i, end = " ")