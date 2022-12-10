def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    i = 0
    count1 = 0
    count2 = 0
    count3 = 0
    result = []
    for i in range(len(answers)):
        if one [i%len(one)] == answers[i]:
            count1 += 1
        
    for i in range(len(answers)):
        if two [i%len(two)] == answers[i]:
            count2 += 1
    for i in range(len(answers)):
        if three [i%len(three)] == answers[i]:
            count3 += 1
    m = max(count1,count2,count3)
    if count1 == count2 and count2 == count3 and m == count1:
        return [1,2,3]
    if count1 == count2 and m == count1:
        return [1,2]        
    if count2 == count3 and m == count2:
        return [2,3]
    if count1 == count3 and m == count3:
        return [1,3]

    if max(count1, count2, count3) == count1:
        return [1]
    if max(count1, count2, count3) == count2:
        return [2]
    if max(count1, count2, count3) == count3:
        return [3]
    


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))