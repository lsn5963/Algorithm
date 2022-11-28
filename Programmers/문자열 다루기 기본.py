def solution(s):
    if len(s) == 4 or len(s) == 6:
        pass
    else:
        return False
        
    for i in s:
        try:
            t = int(i)
        except:
            return False
    return True
print(solution("1234"))
print(solution("56e4"))
print(solution("qwefsd"))
print(solution("12345e"))
print(solution("54632j"))
print(solution("00000"))