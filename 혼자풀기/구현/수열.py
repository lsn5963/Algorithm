n, m = map(int,input().split())
data = list(map(int, input().split()))
tmp = []
lt = 0
rt = m
tmp.append(sum(data[lt:rt]))
for i in range(len(data)-m):
    # print(tmp)
    tmp.append(tmp[-1]-data[lt]+data[rt])
    lt += 1
    rt += 1
print(max(tmp))