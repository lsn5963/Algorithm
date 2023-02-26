n,m = map(int, input().split())

def DFS(v):
    global cnt
    if m == v:
        if len(set(res)) != len(res):
            return
        else:
            for i in range(m):
                print(res[i+1], end= " ")
        print()
        cnt += 1
    else:
        for i in range(n):
            res[v+1] = i+1
            DFS(v+1)

res = [0] *(m+1)
cnt = 0
DFS(0)
print(cnt)




























# import sys
# def DFS(v):
#     if v ==  m:
#         for i in range(m):
#             print(res[i], end= " ")
#         print()
#     else:
#         for i in range(n):
#             if ch[i] == 0:
#                 res[v] = i+1
#                 ch[i] = 1
#                 DFS(v+1)
#                 ch[i] = 0
#     # return

# n,m = map(int,input().split())

# ch = [0] * n
# res = [0] * m
# DFS(0)

# 강사풀이





