n,k = map(int, input().split())
data = []
for i in range(1,n+1):
    if n % i == 0:
        data.append(i)

if len(data) < 4:
    print(-1)
else:
    print(data[k-1])