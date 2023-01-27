def solution(s):
    t = []
    count = 0
    c = 0
    sum = s
    while True:
        if len(sum) == 1:
            break
        c += 1
        
        for i in sum:
            if i == "1":
                t.append(i)
            else:
                count += 1

        num = len(t)
        sum = ""
        t = []
        while num != 0:
            sum = str(num % 2) + sum
            num = num // 2
    return c,count
    