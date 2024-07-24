a = list(input())
b = list(input())

rst = {}
for i in a:
    if i in rst:
        rst[i] += 1
    else:
        rst[i] = 1

for i in b:
    if i in rst:
        rst[i] -= 1


# print(rst)
for a,b in rst.items():
    if b != 0:
        print("NO")
        break
else:
    print("YES")