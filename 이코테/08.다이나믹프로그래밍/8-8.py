import sys
n, m = map(int,sys.stdin.readline().rstrip().split())

data= []
count = 0
for _ in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort(reverse=True)

check = [0] * 10001
result = m
count = 0


for i in data:
    if check[i] == 0:
        if i <= result:
            count = result // i
            result = result % i
            check[i] = 1 

if result == 0:
    print(count)
else:
    print("-1")

"""
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
"""

"""
이문제는 이해를 완벽하게 하지 못했다.
정말 어떻게 이런생각으로 문제를 푸나 신기하다.
다음번에 이런문제가 나온다면 조금 더 쉽게 접근할 수는 있을 것 같다.
"""