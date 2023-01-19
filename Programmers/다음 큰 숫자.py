def solution(n):
    sum = ""
    num = n + 1
    
    while n != 0:
        data = n % 2
        n = n // 2
        sum = str(data) + sum
        
    sum = ""
    count = sum.count("1")
    while True:
        start = num
        while start != 0:
            data = start % 2
            start = start // 2
            sum = str(data) + sum
        
        if count == sum.count("1"):
            return num        
        else:
            sum = ""
            num += 1

print(solution(78))