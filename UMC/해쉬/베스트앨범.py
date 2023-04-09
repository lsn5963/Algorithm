def solution(genres, plays):
    dt = {}
    for i in range(len(genres)):
        if genres[i] in dt:
            dt[genres[i]] = plays[i]
        else:
            dt[genres[i]] += plays[i]
    # print(1)
    # return dt.keys()
print(solution(["classic", "pop", "classic", "classic", "pop"]	,[500, 600, 150, 800, 2500]))