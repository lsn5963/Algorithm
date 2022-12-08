def solution(x, n):
    sum = x
    answer = []
    for i in range(n):
        answer.append(sum)
        sum += x
    return answer

print(solution(2,5))
print(solution(4,3))