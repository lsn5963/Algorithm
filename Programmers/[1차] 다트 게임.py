def solution(dartResult):
    num = 0
    data = []
    count = -1
    n = 0

    for i in dartResult:

        if i=="S":
            data.append(num)
        elif i=="D":
            data.append(num**2)
        elif i=="T":
            data.append(num**3)
        elif i == "*":
            data[count] = data[count] * 2
            if count == 0:
                continue
            data[count-1] = data[count-1] * 2
        elif i == "#":
            data[count] = data[count] * -1
        else:
            count += 1
            if i == "0":
                if dartResult[n-1] == "1":
                    i = 10
            num = int(i)
        n += 1
    # return sum(data)
    return sum(data)

print(solution('10D10S0D'))