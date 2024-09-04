cnt = 0


def solution(numbers, target):
    def dfs(l, sum):
        global cnt
        if l == len(numbers):
            if sum == target:
                cnt += 1
            return

        else:
            dfs(l + 1, sum + numbers[l])
            dfs(l + 1, sum - numbers[l])

    dfs(0, 0)
    return cnt