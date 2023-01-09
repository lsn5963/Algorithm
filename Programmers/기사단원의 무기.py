import math 
def solution(number, limit, power):
    count = 0
    data = []
    for num in range(1, number+1):
        
        for i in range(1,  int(math.sqrt(num))+1):
            if num % i == 0:
                count += 1
                if i ** 2 != num:
                    count += 1
        data.append(count)
        count = 0
    result = []
    for i in data:
        if i > limit:
            result.append(power)
        else:
            result.append(i)
    return sum(result)