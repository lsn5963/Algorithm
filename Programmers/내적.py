def solution(a, b):
    sum = 0
    for i in range(len(a)):
        sum += a[i] * b[i]
    return sum

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))