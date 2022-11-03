import sys
data = []
for _ in range(5):
    data.append(int(sys.stdin.readline().rstrip()))
data.sort()

print(sum(data)//5)
print(data[5//2])