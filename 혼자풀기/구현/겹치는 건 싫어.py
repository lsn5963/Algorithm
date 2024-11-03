from collections import defaultdict
n, k = map(int,input().split())
data = list(map(int,input().split()))
q = [0]*(100001)
lt = 0
rt = 0
rst = 0

while lt <= rt:
    if rt == n:
        rt = rt - 1
        q[data[lt]] -= 1
        lt += 1
        continue
    if q[data[rt]] < k:
        q[data[rt]] += 1
        rst = max(rst,rt-lt + 1)
        rt += 1
    else:
        q[data[lt]] -= 1
        lt += 1
print(rst)