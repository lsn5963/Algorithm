import sys

data = list(map(int,sys.stdin.readline().rstrip().split()))

temp = []
k = []
for i in data:
    if i not in temp:
        temp.append(i)
    else:
        k.append(i)
n = len(temp)

if n == 1:
    print(10000+temp[0]*1000)
elif n == 2:
    print(1000+k[0]*100)
else:
    print(max(temp)*100)

