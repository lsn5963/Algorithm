import heapq


def solution(n, works):
    answer = 0
    q = []
    for i in works:
        heapq.heappush(q, -i)

    while n > 0:
        tmp = heapq.heappop(q)
        if tmp == 0:
            return 0
        tmp += 1
        heapq.heappush(q, tmp)
        n -= 1
    total = 0
    for i in q:
        total += i ** 2
    return total
    # print(q)