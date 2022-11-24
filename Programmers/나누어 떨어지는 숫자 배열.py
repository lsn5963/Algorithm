def solution(arr, divisor):
    answer = []
    if divisor == 1:
        return sorted(arr)
    for i in arr:
        if i % divisor == 0:
            answer.append(i)

    if len(answer) == 0:
        return [-1]
    answer.sort()
    
    return answer

print(solution( 	[2, 36, 1, 3], 1))