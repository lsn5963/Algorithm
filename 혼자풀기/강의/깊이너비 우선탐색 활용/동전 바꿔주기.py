t = int(input())
k = int(input())

data = [list(map(int,input().split())) for _ in range(k)]


cnt = 0
def dfs(l, sum):
    # print(sum)
    global cnt
    if sum > t:
        return
    if sum == t:
        cnt += 1
        return
    if l == k:
        if sum == t:
            cnt += 1
        return


    for i in range(data[l][1]+1):
        dfs(l+1,sum+i*data[l][0])




dfs(0,0)
print(cnt)