def solution(numbers):
    numbers = list(map(str, numbers))
    # data = []
    # for num in numbers:
    #     data.append(num*3)
    # print(data)
    numbers.sort(key = lambda x: x*3, reverse = True)
    
    numbers = ''.join(numbers)
    return str(int(numbers))