import sys
input = sys.stdin.readline().strip

n = input()

result = 1
n = list(map(int, n))
if 0 not in n:
    for i in n:
        result *= i
else:
    for i in n:
        if i == 0 or i == 1:
            result += i
        else:
            result *= i
print(result)

"""
이문제는 i == 1인 경우를 생각하지 못하였다.하지만 나머지 풀이들은 다 맞은 풀이였다.
"""