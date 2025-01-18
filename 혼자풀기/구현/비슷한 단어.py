n = int(input())
data = [input() for _ in range(n)]
check = data[0]
rst = 0
for i in range(1, n):
    check = list(data[0])
    # print(check)
    tmp = data[i]
    cnt = 0
    for j in tmp:
        if j in check:
            (check.remove(j))
        else:
           cnt += 1
    if cnt < 2 and len(check) < 2:
        rst+=1
print(rst)