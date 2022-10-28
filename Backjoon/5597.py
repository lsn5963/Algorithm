import sys
data = []
for _ in range(28):
    data.append(int(sys.stdin.readline()))

data.sort()

for i in range(1,31):
    if i not in data:
        print(i)