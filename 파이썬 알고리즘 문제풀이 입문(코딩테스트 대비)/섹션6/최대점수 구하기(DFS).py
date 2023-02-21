def DFS(l, sum, time):
    if l == n:
        if time <= m:
            rst.append(sum)
    else:
        DFS(l+1,sum+data[l][0], time+data[l][1])
        DFS(l+1,sum, time)
n , m = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(n)]

rst = []
DFS(0,0,0)
print(max(rst))

# def DFS(l, sum, time):
#     rst.append(1)


# rst = []
# DFS(0,0,0)
# print((rst))