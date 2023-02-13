data = [list(map(int, input().split())) for i in range(7)]
cnt = 0
for i in range(7):
    for j in range(3):
        data1 = data[i][j:j+5]
        data2 = []
        for k in range(5):
            data2.append(data[j+k][i])

        if data1 == data1[::-1]:
            cnt += 1
        
        if data2 == data2[::-1]:
            cnt += 1


print(cnt)