from collections import Counter
def solution(want, number, discount):
    rst = {}
    for i in range(len(number)):
        rst[want[i]] = number[i]
    # print(rst)
    n = len(discount) - 10
    cnt = 0
    for i in range(n+1):
        tmp = Counter(discount[i:i+10])
        # print(tmp[0])
        ncnt = 0
        for i in rst:
            if tmp[i] == rst[i]:
                ncnt += 1
        if ncnt == len(want):
            cnt += 1
    return cnt