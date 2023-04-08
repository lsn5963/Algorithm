def solution(clothes):
    data = {}
    for i in clothes:
        if i[1] in data:
            data[i[1]] += 1
        else:
            data[i[1]] = 1
    cnt = 1
    for i in data.keys():
        cnt *= (data[i]) + 1
    return cnt - 1