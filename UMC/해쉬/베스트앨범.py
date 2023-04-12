def solution(genres, plays):
    dt = {}
    csum = {}
    for i,j in enumerate(genres):
        if genres[i] in dt:
            dt[genres[i]].append([plays[i],i])
        else:
            dt[genres[i]] = [[plays[i],i]]
    for i in range(len(genres)):
        if genres[i] in csum:
            csum[genres[i]] += plays[i]
        else:
            csum[genres[i]] = plays[i]
    csum = sorted(csum.items(), key = lambda x: x[1], reverse = True)
    result = []
    for i in csum:
        dt[i[0]] = sorted(dt[i[0]], key = lambda x:x[0] , reverse = True)
        for j in range(2):
            if len(dt[i[0]]) == 1:
                result.append(dt[i[0]][0][1])
                break
            result.append(dt[i[0]][j][1])
    return result
print(solution(["classic", "classic", "classic", "classic", "pop"]	,[500, 150, 800, 800, 2500]))

