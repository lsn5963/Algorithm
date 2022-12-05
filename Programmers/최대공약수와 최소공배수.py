def solution(n, m):
    # goyak = []
    # chgoyak = []
    # for i in range(1,n+1):
    #     if n % i == 0:
    #         goyak.append(i)

    # for i in range(1,m+1):
    #     if m % i == 0:
    #         if i in goyak:
    #             chgoyak.append(i)

    # return max(chgo)
    num = 2
    numlist = []
    count = 0
    for i in range(max(n,m)):
        count += 1
        if n % num == 0 and m % num == 0:
            n = n // num
            m = m // num
            numlist.append(num)
            num = 2
        else:
            num += 1

    if numlist == []:
        return [1,n*m]
    # print(numlist)
    sum = 1
    for i in numlist:
        sum *= i
    temp = sum
    sum = sum * n * m
    return [temp,sum]
    


print(solution(3,12))
print(solution(2,5))
print(solution(84,120))
print(solution(9,18))