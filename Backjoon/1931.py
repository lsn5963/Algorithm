# import sys
# n = int(sys.stdin.readline().rstrip())
# data = []

# for i in range(n):
#     data.append(list(map(int,sys.stdin.readline().rstrip().split())))
# data.sort(key = lambda x : x[1])
# temp = data[0][1] - data[0][0]
# i = 1
# end = 1 #1번째 index
# count = 0
# c = 0
# index = 0
# while(i != n):
#     if temp > (data[i][1] - data[i][0]):
#         end = data[i][1]
#         count += 1
#         temp = data[i][1] - data[i][0]
#         for k in data:
#             if k[0] >= end:
#                 i = c
#                 break
#             c += 1

#     i += 1
# print(count)


import sys
n = int(sys.stdin.readline().rstrip())
data = []

for i in range(n):
    data.append(list(map(int,sys.stdin.readline().rstrip().split())))

data.sort(key = lambda x : (x[1], x[0]))
count = 1
end = data[0][1]
for i in range(1, n):
    if data[i][0] >= end:
        count +=1
        end = data[i][1]
print(count)

"""
정렬을 해서 접근하는것 까지는 성공을 했지만 
또한번 더 해야된다는 것은 생각하지 못하였다,
아쉽다,
"""

