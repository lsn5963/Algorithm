def solution(citations):
    data = []
    
    for h in range(len(citations)+1):
        isang = 0
        iha = 0
        for j in citations:
            if h <= j:
                isang += 1
            else:
                iha += 1
        if isang >= h and iha <= h:
            data.append(h)
    return max(data)
        