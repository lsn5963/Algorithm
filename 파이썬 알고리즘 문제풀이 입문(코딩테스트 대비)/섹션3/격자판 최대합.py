n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))
result = []

for i in range(n):
    sum = 0
    for j in range(n):
        sum += data[i][j]
    result.append(sum)

for i in range(n):
    sum = 0
    for j in range(n):
        sum += data[j][i]
    result.append(sum)

sum = 0
for i in range(n):
    sum += data[i][i]
result.append(sum)

sum = 0
i = 0
j = n-1
for i in range(n):
    sum += data[i][j]
    i += 1
    j -= 1
result.append(sum)


print(max(result))

