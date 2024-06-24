n = int(input())
data = [input() for _ in range(n)]
num = 0
for d in data:
    d = d.upper()
    num += 1
    tmp = d[::-1]
    print("#", end="")
    for i in range(len(tmp)):
        if d[i] != tmp[i]:
            print(num," ","NO")
            break
    else:
        print(num, " ", "YES")

