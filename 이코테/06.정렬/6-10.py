n = int(input())

data = []
for i in range(n):
    data.append(int(input()))

data.sort()
data.reverse()

for i in data:
    print(i , end= " ")

"""
풀이랑 비슷한 식이다
쉬웠다.
"""
