
n, k  = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

"""
n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
"""

"""
쉬운 문제 인것 같았는데 정답을 맞추고 답지를 보았다
답지를 봤는데 코드가 달라서 고민을 해봤더니 테스트코드를 생각하지 못했다
b가 a의 숫자보다 모두 다 숫자가 작으면 a의 합만 도출하면 된다.
이걸 생각하지 못했다.
앞으로는 테스트코드를 잘 생각해봐야겠다.
"""
