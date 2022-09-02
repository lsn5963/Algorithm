n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = max(data) # 큰 수 저장
second = data[-2] # 두번째로 큰 수 저장

count = 0
sum  = 0
for q in range(0, m):
    for t in range(0,k):
        if count == m:  # 큰 수 더하기
            break
        count= count + 1
        sum += first
    if count == m:  # 작은 수 더하기
        break
    count= count + 1
    sum += second
print(sum)

        
"""
파이썬을 오래만에 써봐서 익숙치 않았다.
m값과 k값을 어떻게 하면 따로 분리하여서 계산하는지에 대해 시간을 오래 쓴 것 같다.
다행히 코드는 정답과 똑같았는데 수열로 푸는 부분은 이해하기 어려울 정도로 어려운 코드인 것 같다.
"""
