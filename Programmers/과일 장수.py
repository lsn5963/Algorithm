def solution(k, m, score):
    score.sort(reverse = True)
    num = len(score) // m
    j = 0
    s = 0
    for i in range(num):
        s += min(score[j:j+m]) * m
        j += m
    return s