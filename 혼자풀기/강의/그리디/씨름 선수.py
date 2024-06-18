n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort(reverse = True)
# tmp = n

# for i in range(n):
#     for j in range(i+1,n):
#         if data[i][1] < data[j][1]:
#             tmp -= 1
#             break
tmp = 0
cnt = 0
for k,w in data:
    if tmp < w:
       cnt += 1
       tmp = w
print(cnt)
