data = [list(map(int, input().split())) for _ in range(7)]
# print(data)
cnt = 0
for i in range(7):
    for j in range(3):
        # for k in range(5):
        htmp = data[i][j:j+5]
        # print(htmp)
        rhtmp = htmp[::-1]

        if htmp == rhtmp:
            cnt += 1
for i in range(3):
    for j in range(7):
        ytmp = []
        for k in range(5):
            ytmp.append(data[i+k][j])
        rytmp = ytmp[::-1]

        if ytmp == rytmp:
            cnt += 1


print(cnt)