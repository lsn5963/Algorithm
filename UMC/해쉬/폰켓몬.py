def solution(nums):
    l = len(nums) // 2
    sl = len(set(nums))

    if l > sl:
        return l
    else:
        return sl