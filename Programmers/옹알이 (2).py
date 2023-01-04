from itertools import permutations
def solution(babbling):
    data = ["aya", "ye", "woo", "ma"]
    count = 0

    for i in babbling:
        for j in data:
            if j * 2 not in i:
                i = i.replace(j," ")
        if len(i.strip()) == 0:
            count += 1
    return count

# print(solution(["aya", "yee", "u", "maa"]))
# print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(["wooyemawooye", "mayaa", "ymaeaya"]))