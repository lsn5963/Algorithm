# n,m = map(int,input().split())
# data = list(map(int,input().split()))
# visited =[False] * n
# check = [0] * n
# rst = 0
# def dfs(l):
#     global rst
#     if l == 3:
#         if sum(check) <= m:
#             rst = max(rst,sum(check))
#         return
#
#
#     for i in range(n):
#         if visited[i] == False:
#             visited[i] = True
#             check[l] = data[i]
#             dfs(l+1)
#             visited[i] = False
#
#
#
#
# dfs(0)
# print(rst)

n,m = map(int,input().split())
data = list(map(int,input().split()))
visited =[False] * n
check = [0] * n
rst = 0
def dfs(l,s):
    global rst
    if l == 3:
        if sum(check) <= m:
            rst = max(rst,sum(check))
        return


    for i in range(s,n):
        check[l] = data[i]
        dfs(l+1,i+1)




dfs(0,0)
print(rst)