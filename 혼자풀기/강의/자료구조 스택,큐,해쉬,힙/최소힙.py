import heapq as hq

n = -2
q = []

while n!=-1:
    n = int(input())

    if n == 0:
        if len(q) == 0:
            print(-1)
        else:
            print(hq.heappop(q))
    else:
        hq.heappush(q,n)
