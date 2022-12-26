def solution(a, b, n):
    sum = 0
    while True:
        if n < a:
            break

        num = n // a * b
        n = num + n % a
        sum += num
    return sum

        


print(solution(2,1,20))
print(solution(3,1,20))