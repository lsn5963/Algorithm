n,m = map(int, input().split())

data = list(map(int, input().split()))
count = 0
for i in range(n):
    sum = 0
    sum += data[i]
    if sum == m:
        count += 1
        continue
    for j in range(i+1, n):
        if sum + data[j] == m:
            count += 1
            break
        elif sum + data[j] < m:
            sum += data[j]
        else:
            break
            

print(count)