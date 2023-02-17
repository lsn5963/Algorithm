n = input()
stack = []
sum = 0
for i in n:
    if i == "(":
        stack.append("(")
        last = "("
    else:
        if last == "(":
            stack.pop()
            sum += len(stack)
            last = ")"
        else:
            last = ")"
            stack.pop()
            sum += 1
            last = i

print(sum)