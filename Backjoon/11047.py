import sys

n, k = map(int, sys.stdin.readline().rstrip().split())

data = []

for i in range(n):
    data.append(int(sys.stdin.readline().rstrip()))

data.sort(reverse= True)

result = k
count = 0

for i in range(n):
    if result - data[i] >= 0:
        count +=  result // data[i]
        result %= data[i]
print(count)

"""
정답을 맞췄다.

풀이는 큰값이 들어오는 경우를 대비하여 if문을 사용하여 양수일때만 계산을 하게 하였다.
근데 구글링을 해보니 //연산을 하든 나머지연산을 하든 어떤 값이든 그대로 계산할 수 있기 때문에
if문을 지워도 된다.
나중에 한번더 생각을 해봐야겠다. 
"""
