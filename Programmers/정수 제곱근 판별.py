import math
def solution(n):
    if n ==1:
        return 4
    for i in range(1,n):
        if i**2 == n:
            return (i+1)**2
    return -1

def nextSqure(n):
    sqrt = n ** (1/2)
    print(sqrt)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return 'no'


print(nextSqure(2))