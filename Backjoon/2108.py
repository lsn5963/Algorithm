import sys
n = int(sys.stdin.readline().rstrip())

data = []
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

sum = sum(data)
print(round(sum/n))

data.sort()

print(data[n//2])

# va = []
# c = []
# for i in data:
#     if i not in va:
#         va.append(i)
#         # c.append(data.count(i))

dic = dict()

for i in data:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = max(dic.values())
dic_max = []
for i in dic:
    if m == dic[i]:
        dic_max.append(i)

if len(dic_max) == 1:
    print(dic_max[0])
else:
    print(dic_max[1])

print(max(data)-min(data))

"""
이문제는 최빈값에서 많이 시간을 잡아 먹었다.
시간초과가 나와서 당황했다.
구글링을 통해 dict로 해결하였다. 
dict 접근법을 알게되었다.
"""