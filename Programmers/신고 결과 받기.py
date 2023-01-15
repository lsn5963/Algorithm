def solution(id_list, report, k):
    reported = [[] for _ in range(len(id_list))]
    report = set(report)

    id = []
    singo = {}
    stop = []
    
    for i in report:
        i = i.split(" ")
        singo[i[1]] = 0
        reported[id_list.index(i[0])].append(i[1])

    for i in report:
        i = i.split(" ")
        singo[i[1]] += 1
        
    for i in singo.keys():
        if singo[i] >= k:
            stop.append(i)


    num = []
    for i in reported:
        count = 0
        for j in stop:
            if j in i:
                count+=1
        num.append(count)

    return num
print(solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2))
print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))