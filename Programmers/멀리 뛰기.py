from itertools import permutations
def solution(n):
    s = [0] * (n+1)
    if n==1 or n==2:
        return n
    s[1] = 1
    s[2] = 2
    for i in range(3, n+1):
        s[i] = s[i-2] + s[i-1]

    return s[n] % 1234567
print(solution(3))
print(solution(4))
print(solution(5))