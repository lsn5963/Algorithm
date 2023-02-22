def DFS(v):
    if v > n:
        for i in range(n+1):
            if check[i] == 1:
                print(i, end = " ")
        print()
    else:
        check[v] = 1
        DFS(v+1)
        check[v] = 0
        DFS(v+1)

n = int(input())
check = [0] * (n+1)
DFS(1)
