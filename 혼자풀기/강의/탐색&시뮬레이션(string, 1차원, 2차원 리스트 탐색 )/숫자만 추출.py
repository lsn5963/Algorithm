from itertools import permutations
n = input()
num = []
for i in n:
    if i.isalpha():
        pass
    else:
        num.append(i)
for i in range(len(num)):
    if num[i] == "0":
        continue
    else:
        num = num[i:]
        break
num = int("".join(num))
print(num)
cnt = 0
for i in range(1,num+1):
    if num % i == 0:
        cnt += 1
print(cnt)