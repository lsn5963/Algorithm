from itertools import permutations
def solution(numbers):
    ans = []
    numbers = list(numbers)
    for i in range(1,len(numbers)+1):
        ans.append(list(permutations(numbers,i)))
    rst = []
    for i in ans:
        for j in i:
            rst.append(int("".join(j)))
    rst= list(set(rst))
    data = []
    for i in rst:
        if i == 0 or i == 1:
            continue
        for j in range(2,i):
            if i%j==0:
                break
        else:
            data.append(i)
    return len(data)