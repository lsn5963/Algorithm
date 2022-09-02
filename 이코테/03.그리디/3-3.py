a, b = map(int, input().split())

data =[]
temp = 0
result = 0
for i in range(0,a):
    data = list(map(int, input().split()))
    temp = min(data)
    if temp > result:
        result = temp
        # 이코드는 result = max(temp, result) 코드로 대체할 수 있다.
print(result)

"""
if문을 간다하게 max코드를 사용하여 줄일 수 있다는 것을 알게되었다.
"""
