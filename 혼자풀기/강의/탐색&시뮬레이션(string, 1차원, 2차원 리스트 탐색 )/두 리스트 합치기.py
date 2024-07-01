n = int(input())
ndata = list(map(int,input().split()))
m = int(input())
mdata = list(map(int,input().split()))
# ans = sorted(ndata+mdata)
a = 0
b = 0
ans = []
for _ in range(n+m):
    if a ==n or b == m:
        if a == n:
            for i in mdata[b:]:
                ans.append(i)
        else:
            for i in mdata[a:]:
                ans.append(i)

        break
    if ndata[a]>mdata[b]:
        ans.append(mdata[b])
        b+=1
    elif ndata[a]<=mdata[b]:
        ans.append(ndata[a])
        a += 1


for i in range(len(ans)):
    print(ans[i], end = " ")