import sys
import heapq

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
graph = [[] for _ in range(V + 1)]
# 비용을 미리 무한대로 초기화
answer = [INF] * (V + 1)
queue = []

# 경로 입력
for i in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append([v, w])

def dijkstra(start):
    answer[start] = 0 # 자기 자신의 비용은 0이기 때문에 처음 부분은 0으로 초기화
    heapq.heappush(queue, [0, start]) # 시작값을 0 으로 초기화(자기 자신이기 때문)

    while queue:
        # 현재 노드, 현재 가중치를 pop한다.
        current_w, current_node = heapq.heappop(queue)

        # 최단 거리가 아닌경우 스킵
        if answer[current_node] < current_w:
            continue

        for next_node, weight in graph[current_node]:
            # 선택된 노드 거쳐서 인접 노드로 가는 가중치
            next_w = current_w + weight

            # 기존의 최소 가중치 보다 더 작다면 교체한다.
            # 그리고 다음 노드에 다음 가중치를 넣어준다.
            if next_w < answer[next_node]:
                answer[next_node] = next_w
                heapq.heappush(queue, [next_w, next_node])

dijkstra(K)

# 첫번째 부터 출력(0번째는 필요 없는값이기 때문에)
for i in answer[1:]:
    print(i if i != INF else "INF")


"""
이해가 되지 않아 그냥 코드를 복붙했다.
다음에는 이걸 수정해서 다시 올려야겠다.
"""