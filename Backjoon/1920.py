n = int(input())
data = list(map(int, input().split()))

m = int(input())
ch = list(map(int, input().split()))

data.sort()

for i in ch:
    lt,rt = 0,len(data)-1
    check = False
    
    while lt<=rt:
        mid = (lt+rt) // 2

        if data[mid] == i:
            print(1)
            check = True
            break
        if data[mid] > i:
            rt = mid - 1
        
        if data[mid] < i:
            lt = mid + 1

    if check == False:
        print(0)

# n = int(input())
# data = list(map(int, input().split()))

# m = int(input())
# ch = list(map(int, input().split()))

# data.sort()

# dic = {}

# for i in data:
#     if i not in dic:
#         dic[i] = 1
#     else:
#         dic[i] += 1

# for i in ch:
#     if i in dic:
#         print(dic[i])
#     else:
#         print(0)
