n = int(input())

data = list(map(int,input().split()))

avg = round(sum(data)/n)
# print(avg)
num = []
min = 1000000
for idx, i in enumerate(data):
    temp = abs(i-avg)
    if temp <= min:
        min = temp
        num.append([i,idx])
print(avg,"D",num)
m = max(num)[0]
# print(m)
result = []
for i in num:
    if i[0] == m:
        result.append(i)
print(avg, result[0][1]+1)

