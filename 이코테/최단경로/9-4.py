import sys

n, m = map(int,sys.stdin.readline().rstrip().split())

INF = int(1e9)

graph = [[INF]*(n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a==b:
            graph[a][b] = 0

for _ in range(m):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, sys.stdin.readline().rstrip().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

answer = graph[1][k]+ graph[k][x]

print(INF)
if answer >= INF:
    print(-1)
else:
    print(answer)

"""
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):   # 거쳐가는 노드
    for a in range(1, n + 1):   # 출발 노드
        for b in range(1, n + 1):   # 도착 노드
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
        if graph[a][b] == 1e9:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=" ")
    print()
"""

"""
이문제는 처음으로 플로이드 위셜을 알아보는 문제였기 때문에 보고 풀었다.
다음에는 같은 유형이 나온 문제가 있다면 쉽게 풀 수 있을 것 같다.
"""
