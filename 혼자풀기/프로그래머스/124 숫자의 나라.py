def solution(n):
    rst = ""
    while n != 0:
        tmp = n % 3
        n = n // 3
        if tmp == 0:
            rst = '4' + rst
            n = n - 1
        else:
            rst = str(tmp) + rst
    return rst