def solution(numbers, hand):
    # data = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    sum = ""
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    l = dic['*']
    r = dic['#']
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            l = dic[i]
            sum += "L"
        elif i == 3 or i == 6 or i == 9:
            r = dic[i]
            sum += "R"
        else:
            left = (abs(dic[i][0]-l[0]) + abs(dic[i][1]-l[1]))
            right = (abs(dic[i][0]-r[0]) + abs(dic[i][1]-r[1]))
            if left > right:
                sum += "R"
                r = dic[i]
            elif left < right:
                sum += "L"
                l = dic[i]
            else:
                if hand == "right":
                    sum += "R"
                    r = dic[i]
                else:
                    sum += "L"
                    l = dic[i]

    return sum
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))