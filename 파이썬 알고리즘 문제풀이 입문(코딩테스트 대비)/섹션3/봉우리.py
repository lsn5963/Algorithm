n = int(input())
result = 0
data = [list(map(int, input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,-1,1]
count = 0
for i in range(n):
    for j in range(n):
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]

            if 0 <= nx < n and 0<= ny < n:
                if data[i][j] > data[nx][ny]:
                    continue
                else:
                    break
        else:
            count += 1

print(count)
# for i in range(n):

#     for j in range(n):
#         count = 0

#         #상
#         if i-1 < 0:
#             count += 1
#         elif data[i][j] > data[i-1][j]:
#             count += 1
#         #하
#         if i+1 == n:
#             count += 1
#         elif data[i][j] > data[i+1][j]:
#             count += 1
#         #좌
#         if j-1 < 0:
#             count += 1
#         elif data[i][j] > data[i][j-1]:
#             count += 1
#         #우
#         if j+1 == n:
#             count += 1
#         elif data[i][j] > data[i][j+1]:
#             count += 1

        
#         if count == 4:
#             result += 1
# print(result)

