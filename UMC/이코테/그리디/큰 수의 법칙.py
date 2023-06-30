n,m,k = map(int,input().split())

data = list(map(int, input().split()))

data.sort()

big = data[-1]
small = data[-2]

sum = 0
cnt = 0
for i in range(m):
    if cnt == k:
        cnt = 0
        sum += small
        # print("check",sum)
    else:
        sum += big
        cnt += 1
print(sum)
