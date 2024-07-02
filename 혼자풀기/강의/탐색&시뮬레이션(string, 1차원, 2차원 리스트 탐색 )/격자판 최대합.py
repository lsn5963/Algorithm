n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]


dae = 0
rdae = 0
mhang = []
myul = []
# 행의 합
for i in range(n):
    hang = 0
    yul = 0
    for j in range(n):
        if i == j:
            dae += data[i][j]
        if i+j == n-1:
            rdae += data[i][j]
        hang += data[i][j]
        yul += data[j][i]
    mhang.append(hang)
    myul.append(yul)
print(max(dae,rdae,max(mhang),max(myul)))