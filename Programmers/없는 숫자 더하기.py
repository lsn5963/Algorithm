def solution(numbers):
    sum  = 0
    for i in range(10):
        if i not in numbers:
            sum += i

    return sum

print(solution([1,2,3,4,6,7,8,0]))