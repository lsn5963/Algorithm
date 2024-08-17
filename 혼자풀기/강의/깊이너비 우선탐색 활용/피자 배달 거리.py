from itertools import combinations
n,m = map(int, input().split())
data = [list(map(int,input().split())) for _ in range(n)]
hs = []
piz = []
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            hs.append((i,j))
        elif data[i][j] == 2:
            piz.append((i,j))
# print(piz)
rst = 1e9
pizcombs = list(combinations(piz,m))
for pizcomb in pizcombs:
    sum = 0
    for h in hs:
        # print(pizza)
        dis = 1e9
        x1,y1 = h[0],h[1]
        for j in pizcomb:
            x2,y2 = j[0],j[1]
            dis =min(dis,abs(x1-x2)+abs(y1-y2))
        sum += dis
        # print(sum,pizza)
    if rst > sum:
        rst = sum
print(rst)