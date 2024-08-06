code = list(map(int,input()))
num = len(code)
code.insert(num,-1)
check = [0]*(num)
cnt = 0
def dfs(n,p):
    global cnt
    if n == num:
        cnt += 1
        for i in range(p):
            print(chr(check[i]+64),end = "")
        print()
    else:
        for i in range(27):
            if code[n]  == i+1 :
                check[p] = i+1
                dfs(n+1,p+1)
            elif i+1>=10 and code[n] == (i+1)//10 and code[n+1] == (i+1)%10:
                check[p] = i+1
                dfs(n+2,p+1)
dfs(0,0)
print(cnt)