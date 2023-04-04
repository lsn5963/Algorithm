n,m = map(int, input().split())
ndata = list(map(int, input().split()))
mdata = [list(map(int, input().split())) for _ in range(m)]

rdata = {}
for i in range(n):
    rdata[i] = ndata[i]
for i,j in mdata:
    sum = 0
    for k in range(i,j+1):
        sum += rdata[k-1]
    print(sum)