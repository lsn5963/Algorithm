def solution(n):
    sum = 0
    while(n!=0):

        sum += n % 10
        n = n // 10
    return sum

print(solution(123))
print(solution(987))