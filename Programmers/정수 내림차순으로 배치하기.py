def solution(n):
    n = list(map(int,str(n)))
    n.sort(reverse=True)

    sum = ""

    for i in n:
        sum += str(i)
    return int(sum)

print(solution(118372))