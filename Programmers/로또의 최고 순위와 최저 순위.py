def solution(lottos, win_nums):
    count = 0
    data = []
    for i in lottos:
        if i in win_nums:
            count += 1
    sum = lottos.count(0)+count
    
    if sum == 6:
        data.append(1)
    elif sum == 5:
        data.append(2)
    elif sum == 4:
        data.append(3)
    elif sum == 3:
        data.append(4)
    elif sum == 2:
        data.append(5)
    else:
        data.append(6)

    if count == 6:
        data.append(1)
    elif count == 5:
        data.append(2)
    elif count == 4:
        data.append(3)
    elif count == 3:
        data.append(4)
    elif count == 2:
        data.append(5)
    else:
        data.append(6)

    return data
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]	))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))