rst = [[-1]*15 for _ in range(5)]
for i in range(5):
    tmp = input()
    for j in range(len(tmp)):
        rst[i][j] = tmp[j]

for i in range(15):
    for j in range(5):
        if rst[j][i] == -1:
            continue
        print(rst[j][i], end = "")



# print([[] for _ in range(15)])