def solution(s):
    count = 0
    sum = ""
    for i in s:
        if i == " ":
            sum += " "
            count = 0
        else:
            if count % 2 == 0:
                sum += i.upper()
            else:
                sum += i.lower()
            count += 1
    return sum
        



print(solution("try hello world"))
