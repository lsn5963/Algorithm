n,m = map(int, input().split())
data = list(map(int,input().split()))

lt = 0
rt = 0
cnt = 0
rst = 0

# for i in range(n):
#     rst = 0
#     for j in range(i,n):
#         rst += data[j]
#
#         if rst == m:
#             cnt += 1
#             break
#         elif rst > m:
#             break

rst = 0
while True:
    if lt >= n or rt >= n:
        break
    # print(lt,rt)
    if rst+data[rt] == m:
        cnt += 1
        lt += 1
        rt = lt
        rst = 0
    elif rst+data[rt] < m:
        rst += data[rt]
        rt += 1
    else:
        lt += 1
        rt = lt
        rst = 0
print(cnt)