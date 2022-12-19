def solution(n):
    temp = ""
    while n> 0:
        num = n % 3
        temp = str(num) + temp
        n = n // 3

    # result = ""

    # for i in temp:
    #     result = i + result

    number = 1
    sum = 0

    for i in temp:
        sum += int(i) * number
        number *= 3
    return sum
print(solution(45))
        