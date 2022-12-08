def solution(n, arr1, arr2):
    tarr1 = []
    tarr2 = []
    sum = ""
    for i in arr1:
        for j in range(n):
            ar = i % 2
            i = i // 2
            sum = str(ar) + sum
        tarr1.append(sum)
        sum = ""
    answer = []
    rst = ""
    for i in tarr1:
        for j in i:
            if j == "0":
                rst += " "
            else:
                rst += "#"
        answer.append(list(rst))
        rst = ""

    for i in arr2:
        for j in range(n):
            ar = i % 2
            i = i // 2
            sum = str(ar) + sum
        tarr2.append(sum)
        sum = ""
    rst = ""
    for i in range(n):
        for j in range(n):
            if tarr2[i][j] == "1":
                if answer[i][j] == " ":
                    answer[i][j] = "#"
    result = []
    temp = ""
    for i in answer:
        for j in i:
            temp += j
        result.append(temp)
        temp = ""
    return result
print(solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10]))