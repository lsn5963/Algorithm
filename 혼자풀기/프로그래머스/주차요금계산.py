def solution(fees, records):
    time = {}
    check = {}

    for record in records:

        t, n, r = record.split()
        if n in time:
            check[n] = r
            time[n] = int(t[0:2]) * 60 + int(t[3:5]) - time[n]
        else:
            check[n] = r
            time[n] = int(t[0:2]) * 60 + int(t[3:5])

    for num, res in check.items():
        if res == "IN":
            time[num] = 1439 - time[num]

    rst = []
    time = dict(sorted(time.items()))

    for num, res in time.items():
        if res <= fees[0]:
            rst.append(fees[1])
        else:
            if (res - fees[0]) % fees[2] == 0:
                rst.append(int(fees[1] + ((res - fees[0]) / fees[2]) * fees[3]))
            else:
                rst.append(int(fees[1] + ((res - fees[0]) // fees[2] + 1) * fees[3]))
    return rst