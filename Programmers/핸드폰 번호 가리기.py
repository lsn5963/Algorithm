def solution(phone_number):
    answer = phone_number[:-4]
    sum = ""
    for i in range(len(answer)):
        sum += "*"

    sum += phone_number[-4:]
    return sum

print(solution("01033334444"))
print(solution("027778888"))