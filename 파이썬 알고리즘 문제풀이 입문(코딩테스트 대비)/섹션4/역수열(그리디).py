n = int(input())
data = list(map(int, input().split()))

tmp = [0]*(n+1)

for i in range(n):
    cnt = 0
    for j in range(1,n+1):
        if cnt == data[i]:
            for k in range(j,n+1):
                if tmp[k] == 0:
                    tmp[k] = i+1
                    break
            break
        if tmp[j] == 0:
            cnt += 1

for i in range(1,n+1):
    print(tmp[i], end= " ")