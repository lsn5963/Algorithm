def solution(ingredient):
    s = []
    count = 0
    for i in ingredient:
        s.append(i)
        if s[-4:] == [1,2,3,1] :
            count += 1
            for i in range(4):
                s.pop()
    return count