

for t in range(10):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0
    # a -> 1
    # b -> 2
    for i in range(100):
        for j in range(100):
            if data[i][j] == 2:
                if i-1>=0:
                    if data[i-1][j] == 0:
                        data[i][j] = 0
                        data[i-1][j] = 2
            elif data[i][j] == 1:
                if i+1<100:
                    if data[i+1][j] == 0:
                        data[i+1][j] = 1
                        data[i][j] = 0
    # for i in range(7):
    #     print(data[i])
    for i in range(100):
        for j in range(100):
            if i+1<100 and data[i][j] == 1 and data[i+1][j] == 2:
                cnt += 1
    print("#",end="")
    print(t+1, cnt)
