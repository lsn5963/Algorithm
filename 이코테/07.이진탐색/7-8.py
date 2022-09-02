import sys
n,m = map(int,(sys.stdin.readline().rstrip().split()))

data = list(map(int, sys.stdin.readline().rstrip().split()))

data.sort()
start = data[0]
count = data[0]

length = []
t = 0
while(count != data[-1]):
    for i in data:
        if i <= count:
            length.append(0)
        else:
            length.append(i%count)
    if sum(length) == m:
        t= count
    length = []
    count += 1
print(t)

"""
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력
n, m = list(map(int, input().split(' ')))
# 각 떡의 개별 높이 정보를 입력
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행 (반복적)
result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡볶이 양 계산
        if x > mid:
            total += x - mid
    # 떡볶이 양이 부족한 경우 더 많이 자르기 (오른쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡볶이 양이 충분한 경우 덜 자르기 (왼쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1
print(start)
print(end)
# 정답 출력
print(result)
"""

"""
이진으로 푸는 문제이지만 나는 다르게 풀어버렸다.
하지만 채점을 하면 시간초과가 날 것 이다.
이진풀이의 해설을 이해하는데 한참 걸렸다.
하지만 이진풀이에 대한 중요성을 알게됐고 다음부터는 이진으로 접근해야겠다.
"""