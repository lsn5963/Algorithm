s = input()
ans = ""
t = []
check = False
for i in s:
    if i == "<":
        check = True
        for _ in range(len(t)):
            ans += t.pop()
    elif i == ">":
        check = False
        for _ in range(len(t)):
            ans += t.pop(0)
        ans += ">"
        continue
    elif i == " " and check == False:
        for _ in range(len(t)):
            ans += t.pop()
        ans += " "
        continue
    t.append(i)
# print(list(ans))
# print(t)
for _ in range(len(t)):
    ans += t.pop()
print(ans)