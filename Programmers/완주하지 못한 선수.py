def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if i == len(completion):
            return participant[i]
        if participant[i] != completion[i]:
            return participant[i]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))