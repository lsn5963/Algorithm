def solution(nums):
    sum = 0
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum += nums[i]+nums[j]+nums[k]
                for t in range(2,sum):
                    if sum % t == 0:
                        break
                else:
                    count += 1
                sum = 0
    return count

# print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))