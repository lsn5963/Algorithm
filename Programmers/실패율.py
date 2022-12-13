def solution(N, stages):
    data = []
    fail = []
    
    result = {}
    num = len(stages)
    for i in range(1,N+1):
        data.append(stages.count(i))
   
    for i in range(N):
        if num <= 0:
            fail.append(0)
        else:
            fail.append(data[i] / num)
        num = num - data[i]
    for i in range(N):
        result[i+1] = fail[i]

    result = dict(sorted(result.items(), key = lambda x : x[1], reverse=True))
    result = result.keys()
    return list(result)