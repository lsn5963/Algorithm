n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]

m = int(input())

for _ in range(m):
    h,d,num = map(int,input().split())

    for _ in range(num):
        if d == 1:
            data[h-1][0],data[h-1][1:] = data[h-1][n-1],data[h-1][:n-1]
        else:
            data[h - 1][n-1], data[h - 1][:n-1] = data[h - 1][0], data[h - 1][1:]

s = 0
e = n-1
rst = 0
for i in range(n):
    # print(s,e)
    rst += sum(data[i][s:e+1])
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(rst)