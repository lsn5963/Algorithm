import heapq

import sys

n, e = map(int, sys.stdin.readline().rstrip().split())

INF = int(1e9)
graph = [[] for _ in range(n+1)]


for i in range(e):
    a,b,c = map(int, sys.stdin.readline().rstrip().split())
    # graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    graph[a].append([b,c])
    graph[b].append([a,c])

v1,v2 = map(int, sys.stdin.readline().rstrip().split())

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
    distance[start] = 0
    heapq.heappush(q,(0, start))

    while q:
        len, node = heapq.heappop(q)
        if len > distance[node]:
            continue
        
        for next, val in graph[node]:
            cost = len + val
            if distance[next] > cost:
                distance[next] = cost
                heapq.heappush(q,(cost, next))
    return distance

one = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

path1 = one[v1] + v1_distance[v2] + v2_distance[n]
path2 = one[v2] + v2_distance[v1] + v1_distance[n]
rst = min(path1, path2)

if rst <INF:
    print(rst)
else:
    print(-1)

"""
풀기가 참 어려운 문제다..
답지를 봐도 이해하기 힘들었고 꼭 적응했으면 좋겠다.
"""


