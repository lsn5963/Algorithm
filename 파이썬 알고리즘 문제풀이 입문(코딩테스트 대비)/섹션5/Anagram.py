first = list(input())
second = list(input())

first.sort()
second.sort()

if first == second:
    print("YES")
else:
    print("NO")