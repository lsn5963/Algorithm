def solution(num):
    count = 0
    if num == 1:
        return 0
    for i in range(500):
        if num == 1:
            return count
        if num % 2 == 0:
            num //= 2
        else:
            num = num *3 + 1
        count += 1
    return -1

# print(solution(6))
print(solution(8))
print(solution(626331))