# n = int(input())
# data = list(map(int,input().split()))
# m = int(input())
# data.sort(reverse = True)
# tmp = 0
# for i in data:
#     if m >= i:
#         tmp += m // i
#         m = m % i
# print(tmp)
from collections import deque
def DFS(v,sum):
    global small
    if small < v:
        return
    if sum> m:
        return
    # if small < sum:
    #     return
    if sum == m:
        if small > v:
            small = v
    else:
        for i in data:
            DFS(v+1,sum+i)

n = int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
m = int(input())
small = 21470000000
DFS(0,0)
print(small)

# dq = deque()
# dq.append(0)
# rst = [0]* 10001
# while dq:
#     new = dq.popleft()
#     if new == 15:
#         break
#     for i in range(new+1, new+2, new+5):
#         if rst[i] == 0:
#             rst[i] = rst[new] + 1
#             dq.append(i) 
# print(rst[15])
