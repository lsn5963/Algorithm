num, m = map(int, input().split())

num = list(map(int, str(num)))
stack = []

for i in num:
    while stack and i > stack[-1] and m > 0:
        stack.pop()
        m -= 1
    stack.append(i)
if m > 0:
    stack = stack[:-m]

for i in stack:
    print(i, end= "")