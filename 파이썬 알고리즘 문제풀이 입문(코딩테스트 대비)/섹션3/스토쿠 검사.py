data = [list(map(int, input().split())) for _ in range(9)]

for i in range(9):
    check1 = [0] * 10
    check2 = [0] * 10
    for j in range(9):
        check1[data[i][j]] = 1
        check2[data[j][i]] = 1
    if sum(check1) != 9 or sum(check2) != 9:
        print("NO")
        exit()
for i in range(3):
    for j in range(3):
        check3 = [0] * 10
        for k in range(3):
            for s in range(3):
                check3[data[i*3+k][j*3+s]] = 1
    if sum(check3) != 9:
        print("NO")
        exit()

print("YES")


