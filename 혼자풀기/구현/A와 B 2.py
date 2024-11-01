s = input()
t = input()
def dfs(a,b):
    # print(b)
    if len(a) == len(b):
        if a==b:
            print(1)
            exit()
        return 0
    if b[-1] == "A":
        dfs(a,b[:-1])
    if b[0] == "B":
        dfs(a,b[::-1][:-1])

dfs(s,t)
print(0)

