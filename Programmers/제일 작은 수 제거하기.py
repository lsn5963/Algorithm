def solution(arr):
    mn = min(arr)

    arr.remove(mn)
    if arr == []:
        return [-1]
    return arr

print(solution([4,3,2,1]))
print(solution([10]))