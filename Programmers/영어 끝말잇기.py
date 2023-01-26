def solution(n, words):
    num = 0
    c = 0
    count = 0
    history = []
    t = words[0][0]
    for i in words:
        count += 1
        if t != i[0] or i in history:
            num = count % n
            c = count // n
            if num == 0:
                num =  n
            else:
                c += 1
            t = i[-1]
            break
        else:
            history.append(i)
        t = i[-1]
    return [num,c]
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,["abs","abs"]))