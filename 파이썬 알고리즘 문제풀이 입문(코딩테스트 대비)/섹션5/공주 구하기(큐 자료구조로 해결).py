n,k = map(int, input().split())

data = list(range(1,n+1))
cnt = 0
lt = 0
while len(data) != 1:
    cnt += 1
    if cnt == k:
        data.pop(0)
        cnt = 0
    else:
        
        data.append(data.pop(0))

print(data)