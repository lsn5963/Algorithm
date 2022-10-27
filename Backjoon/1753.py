from cmath import inf
import sys
import heapq

v,e = map(int, sys.stdin.readline().rstrip().split())
INF = int(1e9)
k = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, b, w = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append((b,w))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
"""
다시공부했다. 어떻게 돌아가는지 이해하는게 쉽지않았다.
"""