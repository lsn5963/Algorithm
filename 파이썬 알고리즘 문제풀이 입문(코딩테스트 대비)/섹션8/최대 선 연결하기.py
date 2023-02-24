n = int(input())

data = list(map(int, input().split()))

tmp = sorted(data)

rst = [0] * (n+1)

for i in range(n):
    m = 0
    for j in range(i):
        if data[i] > data[j] and rst[j+1]>m:
            m = rst[j+1]
    rst[i+1] = m+1
print(max(rst))
