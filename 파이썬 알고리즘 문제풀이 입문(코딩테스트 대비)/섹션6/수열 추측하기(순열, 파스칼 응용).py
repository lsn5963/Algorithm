n, f = map(int, input().split())
data = [1]*n
p = [0]*n
check = [0]*(n+1)

def dfs(l, sum):
    if l == n and sum == f:
        for i in p:
            print(i, end = " ")
        exit()
    else:
        for i in range(1,n+1):
            if check[i] == 0:
                check[i] = 1
                p[l] = i
                dfs(l+1, sum+p[l]*data[l])
                check[i] = 0

for i in range(1,n):
    data[i] = data[i-1] * (n-i) // i

dfs(0,0)

