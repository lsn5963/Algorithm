s = input()
t = list(input())
flag = False
while t:
    # print(t)
    if t == list(s):
        flag = True
        break
    if t[-1] == "A":
        t.pop()
    else:
        t.pop()
        t.reverse()
if flag:
    print(1)
else:
    print(0)