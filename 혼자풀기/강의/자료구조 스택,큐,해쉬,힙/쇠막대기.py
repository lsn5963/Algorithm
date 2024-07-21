s = list(input())
data = []

cnt = 0
last = ""
for i in range(len(s)):
    if s[i] == ")":
        if last == "(":
            data.pop()
            cnt += len(data)
        else:
            data.pop()
            cnt += 1
    else:
        data.append("(")
    last = s[i]
    # print(cnt)
print(cnt)