def solution(x):
    t = list(map(int, str(x)))

    if x % sum(t) == 0:
        return True
    else:
        return False

print(solution(10))
print(solution(12))
print(solution(11))