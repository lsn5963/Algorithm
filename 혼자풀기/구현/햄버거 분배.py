# n,k = map(int,input().split())
# data = input()
# loc = []
# for i in range(n):
#     if data[i] == "P":
#         loc.append(i)
# visited= [False]*n
# cnt = 0
# for i in loc:
#     check = False
#     for j in range(k,0,-1):
#         if i-j>=0:
#             if data[i - j] == "H":
#                 if visited[i-j] == False:
#                     visited[i-j] = True
#                     cnt += 1
#                     check = True
#                     break
#         if check == False:
#             if i + j < n:
#                 if data[i + j] == "H":
#                     if visited[i + j] == False:
#                         visited[i + j] = True
#                         cnt += 1
#                         check = True
#                         break
# tmp = cnt
# cnt = 0
# visited= [False]*n
# for i in loc:
#     check = False
#     for j in range(1,k+1):
#         if i-j>=0:
#             if data[i - j] == "H":
#                 if visited[i-j] == False:
#                     visited[i-j] = True
#                     cnt += 1
#                     break
#         if check == False:
#             if i + j < n:
#                 if data[i + j] == "H":
#                     if visited[i + j] == False:
#                         visited[i + j] = True
#                         cnt += 1
#                         check = True
#                         break
# # print(visited)
# print(max(tmp,cnt))
n, k = map(int,input().split())
loc = input()
data= []
for i in range(len(loc)):
    if loc[i] == "P":
        data.append(i)
visited= [False] * n
cnt = 0
for i in data:
    for j in range(i-k,i+k+1):
        if j>=0 and j<n and loc[j] == "H":
            if visited[j] == False:
                visited[j] = True
                cnt += 1
                break
print(cnt)