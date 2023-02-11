n = int(input())
ndata = list(map(int, input().split()))
m = int(input())
mdata = list(map(int, input().split()))

result = []
p1,p2 = 0, 0
while p1 < n and p2 < m:
    if ndata[p1] <= mdata[p2]:
        result.append(ndata[p1])
        p1 += 1
    elif ndata[p1] > mdata[p2]:
        result.append(mdata[p2])
        p2 += 1

if p1 == n:
    result = result + mdata[p2:]
elif p2 == m:
    result = result + ndata[p1:]

for i in result:
    print(i, end = " ")