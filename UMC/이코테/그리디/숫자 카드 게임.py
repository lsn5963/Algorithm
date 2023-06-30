n,m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
tmp = min(data[0])
for dt in data:
    k = min(dt)

    # if k > tmp:
    #     tmp = k

    tmp = max(tmp,k)
print(tmp)