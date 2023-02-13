n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
# spin = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(m):
    a,b,c = map(int, input().split())
    a = a - 1
    if b == 0:
        for i in range(c):
            data[a].append(data[a].pop(0))
    else:
        for i in range(c):
            data[a].insert(0,data[a].pop())

s = 0
e = n
num = 0
for i in range(n):
    num += sum(data[i][s:e])
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(num)