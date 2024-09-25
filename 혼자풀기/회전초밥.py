from collections import deque
n,d,k,c = map(int,input().split())
dishes = [int(input()) for _ in range(n)]
q = (dishes*2)
rst = []
rst = 0
for i in range(n):
    tmp = len(set(q[i:i+k] + [c]))
    rst = max(tmp,rst)
print(rst)
