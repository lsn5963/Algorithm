n = int(input())
data = [input() for _ in range(n)]
for i in data:
    print(i[0]+i[-1])