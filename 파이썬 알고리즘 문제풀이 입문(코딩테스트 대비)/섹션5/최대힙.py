import heapq as hq

a = []

while True:
    n = int(input())
    if n == -1:
        break
    if n == 0:
        if len(a) == 0:
            print(-1)
        else:
            print(-hq.heappop(a))

    else:
        hq.heappush(a,-n) #a리스트에다가 -n을 푸쉬해라

# 기본적으로 heapq는 최소힙으로 작동한다.
# 하지만 이문제는 최대힙 문제이기 때문에 음수의 개념을 활용한다.
