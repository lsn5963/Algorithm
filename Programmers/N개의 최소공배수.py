def solution(arr):
    sum = 1
    for i in arr:
        sum *= i
    for i in range(max(arr), (sum) + 1):
        for j in arr:
            if i % j != 0:
                break
        else:
            return i


print(solution([2,6,8,14]))