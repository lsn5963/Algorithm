n = int(input())
data = list(map(int, input().split()))

m = int(input())
ch = list(map(int, input().split()))

data.sort()

dic = {}

for i in data:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for i in ch:
    if i in dic:
        print(dic[i], end = " ")
    else:
        print(0, end = " ")
