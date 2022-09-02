import sys

def binary(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary(array, target, start, mid -1)
    elif array[mid] < target:
        return binary(array, target, mid + 1, end)


n = int(sys.stdin.readline().rstrip())

na = list(map(int, sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())

ma = list(map(int, sys.stdin.readline().rstrip().split()))

na.sort()
ma.sort()

for m in ma:
    result = binary(na, m, 0, n-1)

    if result != None:
        print("yes", end = " ")
    else:
        print("no", end = " ")

"""
이 문제는 이진탐색으로 푸는 문제이다
이진탐색을 직접 코드로 작성해본적이 없기 때문에 코드를 보면서 작성하였다.
근데 좋은 라이브러리가 있다.
import sys
import bisect

si = sys.stdin.readline
 
n = int(si())
store = sorted(map(int, si().split()))
m = int(si())
wish = list(map(int, si().split()))
print(store,wish)
for x in wish:
    idx = bisect.bisect_left(store, x)
    print("idx", idx)
    if store[idx] == x:
      print('yes')
    else:
      print('no')
bisect를 사용하면 쉽게 풀 수 도 있고 이문제는 set함수를 사용해서도 풀 수 있다.
하지만 set은 이 문제에서만 풀 수 있는 것 같고 이진탐색에서는 사용될지는 모르겠다!
"""

"""
# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# N(가게의 부품 개수) 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백을 기준으로 구분하여 입력
array = list(map(int, input().split()))
array.sort() # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(손님이 확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백을 기준으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')
"""