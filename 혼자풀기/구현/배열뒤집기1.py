n,m,r = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

for _ in range(r):
    for i in range(min(n,m)//2):
        x,y = i,i
        tmp = data[x][y]

        for j in range(i+1,n-i):
            x = j
            prevalue = data[x][y]
            data[x][y] = tmp
            tmp = prevalue

        for j in range(i+1,m-i):
            y = j
            prevalue = data[x][y]
            data[x][y] = tmp
            tmp = prevalue
        print(tmp)
        for j in range(i+1,m-i):
            x = n-j-1
            prevalue = data[x][y]
            data[x][y] = tmp
            tmp = prevalue

        for j in range(i+1,m-i):
            y = m-j-1
            prevalue = data[x][y]
            data[x][y] = tmp
            tmp = prevalue
for i in data:
    for j in i:
        print(j,end= " ")
    print()