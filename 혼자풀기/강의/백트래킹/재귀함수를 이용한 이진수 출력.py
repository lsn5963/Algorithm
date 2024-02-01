n = int(input())

rs = ""
def dfs(n):
    global rs
    if n == 1:
        print("1"+rs)
    else:
        tmp = n % 2
        rs = str(tmp) + rs
        dfs(n//2)
dfs(n)