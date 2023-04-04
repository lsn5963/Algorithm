n,m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(m)]
rst = list(range(1,n+1))
for i in data:
    k = 0
    tmp = rst[i[0]-1:i[1]]
    tmp.reverse()
    for j in range(i[0]-1,i[1]):
        rst[j] = tmp[k]
        k += 1

for i in rst:
    print(i, end = " ")