import sys

data = []
for i in range(9):
    data.append(list(map(int, sys.stdin.readline().rstrip().split())))
t = data[0][0]
a,b = 0, 0
for i in range(9):
    for j in range(9):

        if t < data[i][j]:
            t = data[i][j]
            a,b = i,j

print(t)
print(a+1,b+1)