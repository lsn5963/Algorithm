def solution(k, score):
    data = []
    result = []
    for i in range(len(score)):
        
        if i+1 <= k:
            data.append(score[i])
        elif score[i] >= data[k-1]:
            data.append(score[i])
            
        data.sort(reverse = True)
        data = data[:k]
        result.append(min(data))
    return result