import math
def solution(n):
    count = 0
    for i in range(2,n+1):
        k = int(math.sqrt(i))
        for j in range(2, k+1):
            if i % j == 0:
                break
        else: 
            count += 1
    return count

print(solution(10))
print(solution(5))