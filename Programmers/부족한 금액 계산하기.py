def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        answer = answer + price * i
    
    if answer - money < 0:
        return 0
    else:
        return answer - money

print(solution(3,30,4))