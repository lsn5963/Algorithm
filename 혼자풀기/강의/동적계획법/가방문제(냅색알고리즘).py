n,m = map(int,input().split())

data = [list(map(int,input().split())) for _ in range(n)]
dy= [0]*(m+1)
for i in data:
    for j in range(i[0],m+1):
        dy[j] = max(dy[j],dy[j-i[0]]+i[1])
print(max(dy))