n, k= map(int, input().split())

count = 0
while(True):
    if n == 1:
        break
    if n % k ==0:     
        n = n / k
    else:
        n = n - 1

    count += 1

print(count)

"""
오히려 책에 있는 코드가 더 어렵게 나와서 당황스러운 문제였다.
책에 나온 입력값으로는 답이 정확하게 나오지만 워낙 책에 있는 코드가 복잡해서
다른 입력값을 가져오면 틀릴수도 있겠다는 생각이 들었다.
"""
