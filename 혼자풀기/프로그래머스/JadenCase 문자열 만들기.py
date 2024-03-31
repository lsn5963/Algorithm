def solution(s):
    s = s.split(" ")
    rst = []
    for i in s:
        tmp = []
        for j in range(len(i)):
            if j == 0:
                tmp.append(i[0].upper())
            else:
                tmp.append(i[j].lower())
        rst.append("".join(tmp))
    return " ".join(rst)



