n = int(input())
data = list(map(int, input().split()))
rst = [0]*n

for i in range(1,n+1):
    tmp = data[i-1]
    cnt = 0
    for j in range(n):
        if cnt == tmp and rst[j] == 0:
            rst[j] = i
            break
        elif rst[j] == 0:
            cnt += 1
print(*rst)