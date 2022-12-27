from itertools import combinations
def solution(t, p):
    count = 0
    data = []
    t = list(t)
    for i in range(len(t)):
        sum = ""
        sum += t[i] 
        for j in range(i+1,i+len(p)):
            sum += t[j]
        data.append(sum)
        if i+len(p) == len(t):
            break

    for i in data:
        i = int(i)
        p = int(p)
        if i <= p:
            count += 1
    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))