def solution(clothes):
    data = {}
    for i in clothes:
        if i[1] in data.keys():
            data[i[1]].append(i[0])
        else:
            data[i[1]] = [i[0]]
    count = 1
    for i in data.keys():
        count *= len(data[i]) + 1
        
    return count - 1
    