def solution(s):
    s = list(s)
    s.sort(reverse=True)
    t = ""
    for i in s:
        t += i

    return t

print(solution("Zbcdefg"))