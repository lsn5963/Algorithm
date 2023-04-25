n,b = input().split()
n = n[::-1]
data = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sum = 0
for i in range(len(n)):
    sum += int(b)**i * data.index(n[i])
print(sum)