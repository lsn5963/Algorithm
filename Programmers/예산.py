def solution(d, budget):
    d.sort()
    sum = 0
    count = 0
    for i in d:
        sum += i
        if sum > budget:
            break
        else:
            count += 1

    return count

print(solution([1,3,2,5,4],	9))
print(solution([2,2,3,3],	10))