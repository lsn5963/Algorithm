n = int(input())
data = list(map(int, input().split()))
data.insert(0,0)
res = [0] * (n+1)

res[1] = 1

for i in range(2, n+1):
    m = 0
    for j in range(i-1, 0, -1):
        if data[j]< data[i] and res[j] > m:
            m = res[j]
    res[i] = m + 1

print(max(res))