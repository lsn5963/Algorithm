def solution(numbers):
    sum = []
    numbers.sort()
    for i in range(len(numbers)):
        for t in range(i+1,len(numbers)):
            if numbers[i] +numbers[t] not in sum:
                sum.append(numbers[i] +numbers[t])
    sum.sort()
    return list(sum)

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))
print(solution([0,1]))
        