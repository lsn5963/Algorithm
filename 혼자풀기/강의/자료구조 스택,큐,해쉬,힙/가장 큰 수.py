t,m = map(str, input().split())
n = input()
m = int(m)
n = [int(char) for char in n]

data = [n[0]]

for i in range(1,len(n)):
    while data and data[-1] < n[i] and m>0:
        data.pop()
        m -= 1
    data.append(n[i])

if m>0:
    data = data[:-m]

print("".join(map(str,data)))