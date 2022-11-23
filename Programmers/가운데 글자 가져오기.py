def solution(s):

    answer = ''
    half = len(s)//2
    if len(s)%2 == 0:
        answer = s[half-1:half+1]
    else:
        answer = s[half]
    return answer



# print(solution("qwer"))
# print(solution("abcde"))