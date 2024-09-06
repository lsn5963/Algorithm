def solution(files):
    data = []
    for file in files:
        head, number, tmp = "", "", ""
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break

        for i in range(len(number)):
            if not number[i].isdigit():
                tmp = number[i:]
                number = number[:i]
                break
        data.append([head, number, tmp])

    data.sort(key=lambda x: (x[0].lower(), int(x[1])))
    rst = []
    for i in data:
        rst.append("".join(i))
    return rst