data = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    hdata = []
    ydata = []
    for j in range(9):
        hdata.append(data[i][j])
        ydata.append(data[j][i])
    if len(set(hdata)) != 9 or len(set(ydata)) != 9:
        print("NO")
        exit()
for q in (0,3,6):
    for w in (0, 3, 6):
        sdata = []
        for i in range(3):
            for j in range(3):
                sdata.append(data[i+q][j+w])
        if len(set(sdata)) != 9:
            # print(sdata)
            print("NO")
            exit()

print("YES")

