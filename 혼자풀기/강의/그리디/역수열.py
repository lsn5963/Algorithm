n = int(input())
data = list(map(int, input().split()))
tmp = [0]*(n)

for i in range(1,n+1):
    cnt = -1
    for j in range(n):
        if tmp[j] == 0:
            cnt += 1
        if cnt == data[i-1]:
            # print(i)
            tmp[j] = i
            break

print(*tmp)
