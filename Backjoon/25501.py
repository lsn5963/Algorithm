import sys
from unittest import result

t = int(sys.stdin.readline().rstrip())
data = []
for _ in range(t):
    data.append((sys.stdin.readline().rstrip()))

cnt = 0
def recursion(dt, start, end):
    global cnt
    cnt +=1
    if start >= end:
        return 1
    elif dt[start] != dt[end]:
        return 0
    else:
        return recursion(dt, start+1, end-1)
rst = []
for dt in data:

    temp = recursion(dt,0,len(dt)-1)
    rst.append([temp, cnt])
    cnt = 0

for i in rst:
    print(i[0],i[1])

"""
풀긴 풀었다. 다음은 답을 더 깔금하게 처리해서 풀고싶다.
"""