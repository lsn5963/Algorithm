n,m = map(int,input().split())

sum = 0
data = []
if n > m:
    n,m = m,n
for i in range(1,n+1):
    for j in range(1,m+1):
        data.append(i+j)
# print(data)
dat = set(data)
result = []

for i in dat:
    result.append(data.count(i))
t = max(result)


for i in dat:
    if t == data.count(i):
        print(i, end = " ")
