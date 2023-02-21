def DFS(l,sum):
    if l == n:
        if total - sum == sum:
            print("YES")
            exit(0)
    else:
        sum += data[l]
        DFS(l+1,sum)
        sum -= data[l]
        DFS(l+1,sum)

n = int(input())
data = list(map(int, input().split()))

total = sum(data)
DFS(0,0)
print("NO")