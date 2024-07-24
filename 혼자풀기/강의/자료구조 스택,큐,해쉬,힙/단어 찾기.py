n = int(input())
ans = {}
for _ in range(n):
    tmp = input()
    ans[tmp] = 1
for _ in range(n-1):
    tmp = input()
    ans[tmp] = 0

for key,value in ans.items():
    if value == 1:
        print(key)
        break
