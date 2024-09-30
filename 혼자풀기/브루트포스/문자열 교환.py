s = list(input())
n = len(s)
t = s.count('a')
s = s*2
# print(t)
small = 1e9

for i in range(n):
    tmp = s[i:i+t]
    # print(tmp)
    tbn = tmp.count('b')
    small = min(small,tbn)
print(small)
