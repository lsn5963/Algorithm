def solution(nums):

    answer = 0
    count = len(nums) // 2
    nums = set(nums)

    if len(nums) > count:
        answer = count
        return answer
    else:
        answer = len(nums)
        return answer

nums = [3,3,3,2,2,2]

print(solution(nums))