# def solution(n,a,b):
#     count = 0
#     while b!=a:
#         count += 1
#         a,b = (a+1)//2 ,(b+1)//2
#     return count
def solution(n, a, b):
    result = 1
    if a > b:
        a, b = b, a
    if a % 2 and abs(a-b) == 1:
            return result
    while True:
        if a % 2:
            a = a // 2 +1
        else:
            a = a // 2
        if b % 2:
            b = b // 2 + 1
        else:
            b = b // 2
        result += 1
        if a % 2== 1 and abs(a-b) == 1:
            return result
print(solution(8,3,4))